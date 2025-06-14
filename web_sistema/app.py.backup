from flask import Flask, render_template, jsonify
import sys
import os
import requests
import time
from datetime import datetime
import threading

# Adicionar o diretório pai ao path para importar as estratégias
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from estrategias import EstrategiasDouble, GerenciamentoG1, AnalisadorEstrategias, AnalisadorCompleto

app = Flask(__name__)

# Variáveis globais para o sistema
estrategia = EstrategiasDouble()
gerenciamento = GerenciamentoG1(banca_inicial=100)
analisador_completo = None  # Será inicializado quando necessário
sinal_ativo = None
aguardando_resultado = False
historico_sinais = []
sistema_rodando = False
thread_coleta = None
ultimo_resultado_processado = None

def resultados():
    """Função para coletar resultados da API"""
    cookies = {
        '_gid': 'GA1.2.781127896.1714749072',
        'AMP_MKTG': 'JTdCJTdE',
        '_did': 'web_712234434B09A034',
        'kwai_uuid': '4f8f5347e9db8f1a30e3a0751d616c40',
        '_gcl_au': '1.1.1274132088.1714749077',
        '_fbp': 'fb.1.1714749077202.1498210684',
        'AMP': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI5NTBlMTNlMy05MDBiLTQwMTQtYWE2Yy0xZDY4MWEzOGVmNzYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE0NzQ5MDc0MzA0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNDc0OTA3NDM5MCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMCU3RA==',
        '_ga_LR2H8FWXB7': 'GS1.1.1714757367.3.1.1714757372.0.0.0',
        '_ga': 'GA1.1.1834781342.1714749072',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5,it;q=0.4,es;q=0.3,ru;q=0.2',
        'device_id': '950e13e3-900b-4014-aa6c-1d681a38ef76',
        'ipcountry': 'BR',
        'priority': 'u=1, i',
        'referer': 'https://jonbet.com/pt/games/double',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'session_id': '1714749074304',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-client-language': 'pt',
        'x-client-version': 'v2.280.0',
        'x-kl-kis-ajax-request': 'Ajax_Request',
    }

    try:
        response = requests.get('https://blaze.bet.br/api/singleplayer-originals/originals/roulette_games/recent/1', 
                              cookies=cookies, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return [result['roll'] for result in data]
    except Exception as e:
        print(f"Erro ao coletar resultados: {e}")
    return []

def processar_coleta():
    """Thread para processar coleta de dados"""
    global sinal_ativo, aguardando_resultado, historico_sinais, ultimo_resultado_processado
    
    print("🎯 Sistema de coleta iniciado!")
    
    while sistema_rodando:
        try:
            results = resultados()
            
            if results and len(results) > 0:
                novo_resultado = results[0]  # Resultado mais recente
                
                # Só processar se for um resultado novo
                if ultimo_resultado_processado != novo_resultado:
                    ultimo_resultado_processado = novo_resultado
                    estrategia.adicionar_resultado(novo_resultado)
                    
                    print(f"📈 Novo resultado: {novo_resultado} ({estrategia.cor_do_numero(novo_resultado)})")
                    print(f"📊 Histórico atual: {estrategia.historico[-5:] if len(estrategia.historico) >= 5 else estrategia.historico}")
                    
                    # Se há sinal ativo, verificar resultado
                    if sinal_ativo and aguardando_resultado:
                        cor_resultado = estrategia.cor_do_numero(novo_resultado)
                        
                        # Verificar se acertou
                        acertou = (cor_resultado == sinal_ativo['entrada'] or cor_resultado == 'branco')
                        
                        valor_aposta = gerenciamento.calcular_aposta()
                        resultado_msg = gerenciamento.processar_resultado(acertou, valor_aposta)
                        
                        print(f"🎲 Resultado do sinal: {resultado_msg}")
                        
                        # Adicionar ao histórico
                        historico_sinais.append({
                            'timestamp': datetime.now().strftime('%H:%M:%S'),
                            'sinal': sinal_ativo,
                            'resultado': novo_resultado,
                            'cor_resultado': cor_resultado,
                            'acertou': acertou,
                            'mensagem': resultado_msg
                        })
                        
                        # Se não está mais em gale, finalizar sinal
                        status = gerenciamento.status_banca()
                        if not status['em_gale']:
                            sinal_ativo = None
                            aguardando_resultado = False
                            print("🔄 Sinal finalizado, aguardando novo padrão...")
                    
                    # Se não há sinal ativo, analisar padrões
                    if not sinal_ativo and len(estrategia.historico) >= 4:
                        # Usar o analisador completo (padrão + personalizadas)
                        global analisador_completo
                        if analisador_completo is None:
                            analisador_completo = AnalisadorCompleto(estrategia.historico)
                        else:
                            # Atualizar histórico do analisador
                            analisador_completo.estrategias_padrao.historico = estrategia.historico.copy()
                            analisador_completo.estrategias_personalizadas.historico = estrategia.historico.copy()
                        
                        novo_sinal = analisador_completo.analisar_padroes()
                        
                        if novo_sinal:
                            # Converter formato do sinal para compatibilidade
                            sinal_ativo = {
                                'entrada': novo_sinal['sinal'],
                                'estrategia': novo_sinal['estrategia'],
                                'confianca': novo_sinal['confianca'],
                                'protecao': novo_sinal.get('protecao', 'branco'),
                                'estrategia_id': novo_sinal.get('estrategia_id', None)
                            }
                            aguardando_resultado = True
                            print(f"🚨 SINAL DETECTADO: {novo_sinal['sinal'].upper()} - {novo_sinal['estrategia']} - Confiança: {novo_sinal['confianca']}%")
            
            time.sleep(3)  # Aguardar 3 segundos antes da próxima verificação
            
        except Exception as e:
            print(f"Erro na coleta: {e}")
            time.sleep(5)

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    """API para obter status atual do sistema"""
    global sinal_ativo, aguardando_resultado
    
    # Obter últimos resultados
    results = resultados()
    resultados_formatados = []
    
    for r in results[:10]:  # Últimos 10 resultados
        if r == 0:
            cor = 'branco'
            emoji = '⚪'
        elif 1 <= r <= 7:
            cor = 'vermelho'
            emoji = '🔴'
        elif 8 <= r <= 14:
            cor = 'preto'
            emoji = '⚫'
        else:
            cor = 'desconhecido'
            emoji = ''
        
        resultados_formatados.append({
            'numero': r,
            'cor': cor,
            'emoji': emoji
        })
    
    # Status da banca
    status_banca = gerenciamento.status_banca()
    
    return jsonify({
        'sistema_rodando': sistema_rodando,
        'resultados': resultados_formatados,
        'sinal_ativo': sinal_ativo,
        'aguardando_resultado': aguardando_resultado,
        'historico_estrategia': len(estrategia.historico),
        'banca': status_banca,
        'historico_sinais': historico_sinais[-10:]  # Últimos 10 sinais
    })

@app.route('/api/iniciar')
def api_iniciar():
    """API para iniciar o sistema"""
    global sistema_rodando, thread_coleta
    
    if not sistema_rodando:
        sistema_rodando = True
        thread_coleta = threading.Thread(target=processar_coleta, daemon=True)
        thread_coleta.start()
        print("✅ Sistema iniciado via web!")
        return jsonify({'status': 'iniciado'})
    
    return jsonify({'status': 'ja_rodando'})

@app.route('/api/parar')
def api_parar():
    """API para parar o sistema"""
    global sistema_rodando
    
    sistema_rodando = False
    print("⏹️ Sistema parado via web!")
    return jsonify({'status': 'parado'})

@app.route('/api/reset')
def api_reset():
    """API para resetar o sistema"""
    global estrategia, gerenciamento, sinal_ativo, aguardando_resultado, historico_sinais, ultimo_resultado_processado
    
    estrategia = EstrategiasDouble()
    gerenciamento = GerenciamentoG1(banca_inicial=100)
    sinal_ativo = None
    aguardando_resultado = False
    historico_sinais = []
    ultimo_resultado_processado = None
    
    print("🔄 Sistema resetado via web!")
    return jsonify({'status': 'resetado'})

# ENDPOINTS PARA ESTRATÉGIAS PERSONALIZADAS

@app.route('/api/estrategias')
def api_estrategias():
    """API para obter todas as estratégias personalizadas"""
    global analisador_completo
    
    if analisador_completo is None:
        return jsonify({'estrategias': []})
    
    estrategias = analisador_completo.obter_estrategias_personalizadas()
    return jsonify({'estrategias': estrategias})

@app.route('/api/estrategias/adicionar', methods=['POST'])
def api_adicionar_estrategia():
    """API para adicionar nova estratégia personalizada"""
    from flask import request
    
    global analisador_completo
    
    try:
        data = request.get_json()
        
        if analisador_completo is None:
            analisador_completo = AnalisadorCompleto(estrategia.historico)
        
        tipo = data.get('tipo')
        
        if tipo == 'sequencia':
            estrategia_id = analisador_completo.adicionar_estrategia_personalizada(
                'sequencia',
                nome=data.get('nome'),
                sequencia_cores=data.get('sequencia_cores'),
                apostar_em=data.get('apostar_em'),
                confianca=int(data.get('confianca', 70)),
                descricao=data.get('descricao', '')
            )
        elif tipo == 'numero':
            estrategia_id = analisador_completo.adicionar_estrategia_personalizada(
                'numero',
                nome=data.get('nome'),
                numero_gatilho=int(data.get('numero_gatilho')),
                pedras_esperar=int(data.get('pedras_esperar')),
                apostar_em=data.get('apostar_em'),
                confianca=int(data.get('confianca', 70)),
                descricao=data.get('descricao', '')
            )
        elif tipo == 'contagem':
            estrategia_id = analisador_completo.adicionar_estrategia_personalizada(
                'contagem',
                nome=data.get('nome'),
                cor_contar=data.get('cor_contar'),
                quantidade_minima=int(data.get('quantidade_minima')),
                apostar_em=data.get('apostar_em'),
                confianca=int(data.get('confianca', 70)),
                janela_analise=int(data.get('janela_analise', 10)),
                descricao=data.get('descricao', '')
            )
        else:
            return jsonify({'status': 'erro', 'mensagem': 'Tipo de estratégia inválido'}), 400
        
        print(f"✅ Nova estratégia adicionada: {data.get('nome')} (ID: {estrategia_id})")
        return jsonify({'status': 'sucesso', 'estrategia_id': estrategia_id})
        
    except Exception as e:
        print(f"Erro ao adicionar estratégia: {e}")
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/estrategias/<int:estrategia_id>/toggle', methods=['POST'])
def api_toggle_estrategia(estrategia_id):
    """API para ativar/desativar estratégia"""
    from flask import request
    
    global analisador_completo
    
    if analisador_completo is None:
        return jsonify({'status': 'erro', 'mensagem': 'Nenhuma estratégia encontrada'}), 404
    
    try:
        data = request.get_json()
        ativa = data.get('ativa', True)
        
        analisador_completo.estrategias_personalizadas.ativar_desativar_estrategia(estrategia_id, ativa)
        
        status_text = "ativada" if ativa else "desativada"
        print(f"🔄 Estratégia {estrategia_id} {status_text}")
        
        return jsonify({'status': 'sucesso'})
        
    except Exception as e:
        print(f"Erro ao alterar estratégia: {e}")
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/estrategias/<int:estrategia_id>/remover', methods=['DELETE'])
def api_remover_estrategia(estrategia_id):
    """API para remover estratégia"""
    global analisador_completo
    
    if analisador_completo is None:
        return jsonify({'status': 'erro', 'mensagem': 'Nenhuma estratégia encontrada'}), 404
    
    try:
        analisador_completo.estrategias_personalizadas.remover_estrategia(estrategia_id)
        
        print(f"🗑️ Estratégia {estrategia_id} removida")
        return jsonify({'status': 'sucesso'})
        
    except Exception as e:
        print(f"Erro ao remover estratégia: {e}")
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500



if __name__ == '__main__':
    print("🌐 Iniciando servidor web...")
    print("📱 Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 