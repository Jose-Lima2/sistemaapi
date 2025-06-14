import requests
import time
from estrategias import EstrategiasDouble, GerenciamentoG1, AnalisadorEstrategias

def resultados():

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
        # 'cookie': '_gid=GA1.2.781127896.1714749072; AMP_MKTG=JTdCJTdE; _did=web_712234434B09A034; kwai_uuid=4f8f5347e9db8f1a30e3a0751d616c40; _gcl_au=1.1.1274132088.1714749077; _fbp=fb.1.1714749077202.1498210684; AMP=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI5NTBlMTNlMy05MDBiLTQwMTQtYWE2Yy0xZDY4MWEzOGVmNzYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE0NzQ5MDc0MzA0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNDc0OTA3NDM5MCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMCU3RA==; _ga_LR2H8FWXB7=GS1.1.1714757367.3.1.1714757372.0.0.0; _ga=GA1.1.1834781342.1714749072',
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

    response = requests.get('https://blaze.bet.br/api/singleplayer-originals/originals/roulette_games/recent/1', cookies=cookies, headers=headers)

    if response.status_code == 200:
       data = response.json()
       results =  [result ['roll'] for result in data]
       return results
    
# Inicializar sistema de estratégias
estrategia = EstrategiasDouble()
gerenciamento = GerenciamentoG1(banca_inicial=100)

# Controle de sinais ativos
sinal_ativo = None
aguardando_resultado = False

resultado_anterior = []    
print("🎯 SISTEMA DE SINAIS INICIADO!")
print("📊 Coletando dados para análise de padrões...")
print("-" * 50)

while True: 

    results = resultados()

    if resultado_anterior != results:
        resultado_anterior = results
        
        # Adicionar apenas o resultado mais recente (primeiro da lista)
        if results:
            novo_resultado = results[0]  # O primeiro é o mais recente
            estrategia.adicionar_resultado(novo_resultado)
        
        # Mostrar resultados com cores
        resultados_cores = []
        for r in results:
            if r == 0:
                cor = '⚪'
            elif 1 <= r <= 7:
                cor = '🔴'
            elif 8 <= r <= 14:
                cor = '⚫'
            else:
                cor = ''
            resultados_cores.append(f'{r}{cor}')
        
        print(f"📈 Resultados: {', '.join(resultados_cores)}")
        
        # Se há sinal ativo, verificar resultado
        if sinal_ativo and aguardando_resultado:
            ultimo_resultado = results[0]  # Resultado mais recente
            cor_resultado = estrategia.cor_do_numero(ultimo_resultado)
            
            # Verificar se acertou (cor do sinal ou branco)
            acertou = (cor_resultado == sinal_ativo['entrada'] or cor_resultado == 'branco')
            
            valor_aposta = gerenciamento.calcular_aposta()
            resultado_msg = gerenciamento.processar_resultado(acertou, valor_aposta)
            
            print(f"🎲 {resultado_msg}")
            
            # Se não está mais em gale, finalizar sinal
            status = gerenciamento.status_banca()
            if not status['em_gale']:
                sinal_ativo = None
                aguardando_resultado = False
                print("🔄 Aguardando novo padrão...\n")
        
        # Se não há sinal ativo, analisar padrões
        if not sinal_ativo:
            # Usar o novo analisador de estratégias
            analisador = AnalisadorEstrategias(estrategia.historico)
            novo_sinal = analisador.analisar_padroes()
            
            if novo_sinal:
                # Converter formato do sinal para compatibilidade
                sinal = {
                    'entrada': novo_sinal['sinal'],
                    'estrategia': novo_sinal['estrategia'],
                    'confianca': novo_sinal['confianca'],
                    'protecao': novo_sinal.get('protecao', 'branco'),
                    'gale': 'G1 (2% da banca)'
                }
                print("\n" + "="*60)
                print("🚨 SINAL DETECTADO! 🚨")
                print("="*60)
                
                # Emoji para a cor do sinal
                if sinal['entrada'] == 'vermelho':
                    emoji_sinal = '🔴'
                elif sinal['entrada'] == 'preto':
                    emoji_sinal = '⚫'
                else:
                    emoji_sinal = '⚪'
                
                print(f"🎯 {emoji_sinal} + ⚪")
                print(f"📊 CONFIANÇA: {sinal['confianca']}%")
                print(f"🧠 ESTRATÉGIA: {sinal['estrategia']}")
                print(f"💸 SISTEMA: {sinal['gale']}")
                
                print("="*60)
                print("⏰ Aguardando próximo resultado para confirmar...")
                print()
                
                # Ativar sinal
                sinal_ativo = sinal
                aguardando_resultado = True
            else:
                # Mostrar status sem sinal
                print(f"⏳ Analisando padrões... | Histórico: {len(estrategia.historico)} resultados")
    
    time.sleep(2)

