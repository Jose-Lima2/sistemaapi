# ESTRATÉGIAS DE PADRÕES PARA DOUBLE/ROLETA - ATÉ G1
# Baseado em pesquisas dos melhores padrões utilizados por jogadores experientes

class EstrategiasDouble:
    
    def __init__(self):
        self.historico = []
        self.max_historico = 20  # Mantém os últimos 20 resultados
        
    def adicionar_resultado(self, numero):
        """Adiciona um novo resultado ao histórico"""
        # Só adiciona se for um número novo (evita duplicatas)
        if not self.historico or numero != self.historico[-1]:
            self.historico.append(numero)
            if len(self.historico) > self.max_historico:
                self.historico.pop(0)
    
    def cor_do_numero(self, numero):
        """Retorna a cor do número"""
        if numero == 0:
            return 'branco'
        elif 1 <= numero <= 7:
            return 'vermelho'
        elif 8 <= numero <= 14:
            return 'preto'
        return 'desconhecido'
    
    def cores_historico(self):
        """Retorna lista das cores do histórico"""
        cores = [self.cor_do_numero(num) for num in self.historico]
        return cores
    
    # ESTRATÉGIA 1: PADRÃO DE ALTERNÂNCIA
    def padrao_alternancia(self):
        """
        Detecta padrões de alternância entre cores
        Ex: V-P-V-P -> Próximo: Vermelho
        """
        if len(self.historico) < 4:
            return None
            
        cores = self.cores_historico()[-4:]
        
        # Padrão V-P-V-P
        if cores == ['vermelho', 'preto', 'vermelho', 'preto']:
            return {
                'sinal': 'vermelho',
                'confianca': 75,
                'estrategia': 'Alternância V-P-V-P',
                'protecao': 'branco'
            }
        
        # Padrão P-V-P-V
        if cores == ['preto', 'vermelho', 'preto', 'vermelho']:
            return {
                'sinal': 'preto',
                'confianca': 75,
                'estrategia': 'Alternância P-V-P-V',
                'protecao': 'branco'
            }
        
        return None
    
    # ESTRATÉGIA 2: SEQUÊNCIA DE REPETIÇÕES
    def padrao_repeticoes(self):
        """
        Detecta padrões de repetições
        Ex: V-V-P-P -> Próximo: Vermelho
        """
        if len(self.historico) < 4:
            return None
            
        cores = self.cores_historico()[-4:]
        
        # Padrão V-V-P-P
        if cores == ['vermelho', 'vermelho', 'preto', 'preto']:
            return {
                'sinal': 'vermelho',
                'confianca': 80,
                'estrategia': 'Repetição V-V-P-P',
                'protecao': 'branco'
            }
        
        # Padrão P-P-V-V
        if cores == ['preto', 'preto', 'vermelho', 'vermelho']:
            return {
                'sinal': 'preto',
                'confianca': 80,
                'estrategia': 'Repetição P-P-V-V',
                'protecao': 'branco'
            }
        
        return None
    
    # ESTRATÉGIA 3: QUEBRA DE SEQUÊNCIA
    def padrao_quebra_sequencia(self):
        """
        Detecta quebra de sequências longas
        Ex: V-V-V-P -> Próximo: Preto (continua a quebra)
        """
        if len(self.historico) < 4:
            return None
            
        cores = self.cores_historico()[-4:]
        
        # 3 Vermelhos seguidos + 1 Preto
        if cores == ['vermelho', 'vermelho', 'vermelho', 'preto']:
            return {
                'sinal': 'preto',
                'confianca': 70,
                'estrategia': 'Quebra sequência vermelha',
                'protecao': 'branco'
            }
        
        # 3 Pretos seguidos + 1 Vermelho
        if cores == ['preto', 'preto', 'preto', 'vermelho']:
            return {
                'sinal': 'vermelho',
                'confianca': 70,
                'estrategia': 'Quebra sequência preta',
                'protecao': 'branco'
            }
        
        return None
    
    # ESTRATÉGIA 4: PADRÃO APÓS BRANCO
    def padrao_pos_branco(self):
        """
        Analisa padrões após o branco aparecer
        Branco assume valor da cor anterior
        """
        if len(self.historico) < 3:
            return None
            
        cores = self.cores_historico()
        
        # Se o último foi branco
        if cores[-1] == 'branco' and len(cores) >= 2:
            cor_anterior = cores[-2]
            if cor_anterior in ['vermelho', 'preto']:
                return {
                    'sinal': cor_anterior,
                    'confianca': 65,
                    'estrategia': f'Pós-branco (assume {cor_anterior})',
                    'protecao': 'branco'
                }
        
        return None
    
    # ESTRATÉGIA 5: PADRÃO DE DOMINÂNCIA
    def padrao_dominancia(self):
        """
        Analisa qual cor está dominando nos últimos resultados
        """
        if len(self.historico) < 6:
            return None
            
        cores = self.cores_historico()[-6:]
        vermelhos = cores.count('vermelho')
        pretos = cores.count('preto')
        
        # Se uma cor dominou muito, apostar na outra
        if vermelhos >= 5:
            return {
                'sinal': 'preto',
                'confianca': 60,
                'estrategia': 'Anti-dominância (muitos vermelhos)',
                'protecao': 'branco'
            }
        elif pretos >= 5:
            return {
                'sinal': 'vermelho',
                'confianca': 60,
                'estrategia': 'Anti-dominância (muitos pretos)',
                'protecao': 'branco'
            }
        
        return None
    
    # ESTRATÉGIA 6: PADRÃO FIBONACCI
    def padrao_fibonacci(self):
        """
        Baseado na sequência de Fibonacci aplicada às cores
        1-1-2-3-5... aplicado a repetições de cores
        """
        if len(self.historico) < 5:
            return None
            
        cores = self.cores_historico()[-5:]
        
        # Padrão Fibonacci: V-V-P-P-P (1-1-2 em cores)
        if cores == ['vermelho', 'vermelho', 'preto', 'preto', 'preto']:
            return {
                'sinal': 'vermelho',
                'confianca': 65,
                'estrategia': 'Fibonacci V-V-P-P-P',
                'protecao': 'branco'
            }
        
        # Padrão Fibonacci: P-P-V-V-V (1-1-2 em cores)
        if cores == ['preto', 'preto', 'vermelho', 'vermelho', 'vermelho']:
            return {
                'sinal': 'preto',
                'confianca': 65,
                'estrategia': 'Fibonacci P-P-V-V-V',
                'protecao': 'branco'
            }
        
        return None
    
    # ESTRATÉGIA 7: PADRÃO DE ESPELHO
    def padrao_espelho(self):
        """
        Detecta padrões espelhados
        Ex: V-P-V -> Próximo: P (espelha V-P-V-P)
        """
        if len(self.historico) < 3:
            return None
            
        cores = self.cores_historico()[-3:]
        
        # V-P-V -> P
        if cores == ['vermelho', 'preto', 'vermelho']:
            return {
                'sinal': 'preto',
                'confianca': 70,
                'estrategia': 'Espelho V-P-V',
                'protecao': 'branco'
            }
        
        # P-V-P -> V
        if cores == ['preto', 'vermelho', 'preto']:
            return {
                'sinal': 'vermelho',
                'confianca': 70,
                'estrategia': 'Espelho P-V-P',
                'protecao': 'branco'
            }
        
        return None
    
    # ESTRATÉGIA 8: PADRÃO DE TENDÊNCIA
    def padrao_tendencia(self):
        """
        Analisa tendência geral dos últimos resultados
        """
        if len(self.historico) < 8:
            return None
            
        cores = self.cores_historico()[-8:]
        vermelhos = cores.count('vermelho')
        pretos = cores.count('preto')
        
        # Tendência forte para uma cor - apostar nela
        if vermelhos >= 6:
            return {
                'sinal': 'vermelho',
                'confianca': 55,
                'estrategia': 'Tendência vermelha forte',
                'protecao': 'branco'
            }
        elif pretos >= 6:
            return {
                'sinal': 'preto',
                'confianca': 55,
                'estrategia': 'Tendência preta forte',
                'protecao': 'branco'
            }
        
        return None
    
    # ESTRATÉGIA 9: ESTRATÉGIA DO 7
    def padrao_estrategia_7(self):
        """
        Quando sai o número 7, espera mais 6 pedras sairem
        Na 7ª pedra após o 7, aposta no vermelho até G1
        """
        if len(self.historico) < 8:
            return None
        
        # Procurar pelo número 7 nos últimos resultados
        for i in range(len(self.historico) - 7, len(self.historico)):
            if i >= 0 and self.historico[i] == 7:
                # Encontrou o 7, verificar se já passaram 6 pedras
                pedras_apos_7 = len(self.historico) - i - 1
                
                if pedras_apos_7 == 6:
                    # É a 7ª pedra após o 7, apostar no vermelho
                    return {
                        'sinal': 'vermelho',
                        'confianca': 85,
                        'estrategia': 'Estratégia do 7 (7ª pedra)',
                        'protecao': 'branco'
                    }
        
        return None
    
    # ESTRATÉGIA 10: ESTRATÉGIA DO 6
    def padrao_estrategia_6(self):
        """
        Quando sai o número 6, espera mais 5 pedras sairem
        Na 6ª pedra após o 6, aposta no vermelho até G1
        """
        if len(self.historico) < 7:
            return None
        
        # Procurar pelo número 6 nos últimos resultados
        for i in range(len(self.historico) - 6, len(self.historico)):
            if i >= 0 and self.historico[i] == 6:
                # Encontrou o 6, verificar se já passaram 5 pedras
                pedras_apos_6 = len(self.historico) - i - 1
                
                if pedras_apos_6 == 5:
                    # É a 6ª pedra após o 6, apostar no vermelho
                    return {
                        'sinal': 'vermelho',
                        'confianca': 85,
                        'estrategia': 'Estratégia do 6 (6ª pedra)',
                        'protecao': 'branco'
                    }
        
        return None
    
    def analisar_padroes(self):
        """
        Analisa todos os padrões e retorna o melhor sinal
        """
        estrategias = [
            self.padrao_estrategia_7(),      # Prioridade alta
            self.padrao_estrategia_6(),      # Prioridade alta
            self.padrao_repeticoes(),
            self.padrao_alternancia(),
            self.padrao_quebra_sequencia(),
            self.padrao_espelho(),
            self.padrao_fibonacci(),
            self.padrao_pos_branco(),
            self.padrao_dominancia(),
            self.padrao_tendencia()
        ]
        
        # Filtra estratégias válidas e ordena por confiança
        estrategias_validas = [e for e in estrategias if e is not None]
        
        if estrategias_validas:
            # Retorna a estratégia com maior confiança
            melhor_estrategia = max(estrategias_validas, key=lambda x: x['confianca'])
            return melhor_estrategia
        
        return None
    
    def gerar_sinal(self):
        """
        Gera sinal baseado na melhor estratégia encontrada
        """
        sinal = self.analisar_padroes()
        
        if sinal:
            return {
                'entrada': sinal['sinal'],
                'protecao': sinal['protecao'],
                'confianca': sinal['confianca'],
                'estrategia': sinal['estrategia'],
                'gale': 'G1',  # Até G1 conforme solicitado
                'historico_usado': self.historico[-min(8, len(self.historico)):]
            }
        
        return None

# CONFIGURAÇÕES DE GERENCIAMENTO
class GerenciamentoG1:
    """
    Sistema de gerenciamento para apostas até G1
    """
    
    def __init__(self, banca_inicial=100):
        self.banca_inicial = banca_inicial
        self.banca_atual = banca_inicial
        self.valor_entrada = banca_inicial * 0.02  # 2% da banca
        self.em_gale = False
        self.tentativas_gale = 0
        self.max_gale = 1  # Até G1
        
    def calcular_aposta(self):
        """Calcula valor da aposta (entrada ou gale)"""
        if not self.em_gale:
            return self.valor_entrada
        else:
            # G1: dobra a aposta
            return self.valor_entrada * 2
    
    def processar_resultado(self, acertou, valor_apostado):
        """Processa resultado da aposta"""
        if acertou:
            # Ganhou - recebe 2x a aposta
            ganho = valor_apostado * 2
            self.banca_atual += ganho - valor_apostado
            self.em_gale = False
            self.tentativas_gale = 0
            return f"✅ ACERTOU! Ganho: +{ganho - valor_apostado:.2f}"
        else:
            # Perdeu
            self.banca_atual -= valor_apostado
            
            if self.tentativas_gale < self.max_gale:
                self.em_gale = True
                self.tentativas_gale += 1
                return f"❌ ERROU! Vai para G{self.tentativas_gale}"
            else:
                # Perdeu tudo (entrada + G1)
                self.em_gale = False
                self.tentativas_gale = 0
                return f"💀 STOP! Perdeu entrada + G1: -{valor_apostado:.2f}"
    
    def status_banca(self):
        """Retorna status atual da banca"""
        lucro = self.banca_atual - self.banca_inicial
        percentual = (lucro / self.banca_inicial) * 100
        
        return {
            'banca_atual': self.banca_atual,
            'lucro': lucro,
            'percentual': percentual,
            'em_gale': self.em_gale,
            'tentativa_gale': self.tentativas_gale
        }

# EXEMPLO DE USO
if __name__ == "__main__":
    # Exemplo de como usar as estratégias
    estrategia = EstrategiasDouble()
    gerenciamento = GerenciamentoG1(banca_inicial=100)
    
    # Simulação com alguns resultados
    resultados_exemplo = [5, 12, 3, 9, 1, 11, 2, 8]
    
    for resultado in resultados_exemplo:
        estrategia.adicionar_resultado(resultado)
        print(f"Resultado: {resultado} - Cor: {estrategia.cor_do_numero(resultado)}")
    
    # Gerar sinal
    sinal = estrategia.gerar_sinal()
    if sinal:
        print(f"\n🎯 SINAL DETECTADO!")
        print(f"Apostar em: {sinal['entrada']}")
        print(f"Proteção: {sinal['protecao']}")
        print(f"Confiança: {sinal['confianca']}%")
        print(f"Estratégia: {sinal['estrategia']}")
        print(f"Sistema: {sinal['gale']}")
    else:
        print("\n⏳ Aguardando padrão...")

# CLASSE PARA COMPATIBILIDADE COM SISTEMA WEB
class AnalisadorEstrategias:
    """
    Classe wrapper para compatibilidade com o sistema web
    Usa a mesma lógica da EstrategiasDouble
    """
    
    def __init__(self, historico):
        self.estrategia = EstrategiasDouble()
        # Adicionar histórico existente
        for resultado in historico:
            self.estrategia.adicionar_resultado(resultado)
    
    def analisar_padroes(self):
        """
        Analisa padrões e retorna sinal no formato esperado pelo sistema web
        """
        return self.estrategia.analisar_padroes()

# SISTEMA DE ESTRATÉGIAS PERSONALIZADAS
class EstrategiasPersonalizadas:
    """
    Sistema para criar e gerenciar estratégias personalizadas do usuário
    """
    
    def __init__(self):
        self.estrategias_customizadas = []
        self.historico = []
    
    def adicionar_resultado(self, numero):
        """Adiciona resultado ao histórico"""
        if not self.historico or numero != self.historico[-1]:
            self.historico.append(numero)
            if len(self.historico) > 50:  # Manter últimos 50
                self.historico.pop(0)
    
    def cor_do_numero(self, numero):
        """Retorna a cor do número"""
        if numero == 0:
            return 'branco'
        elif 1 <= numero <= 7:
            return 'vermelho'
        elif 8 <= numero <= 14:
            return 'preto'
        return 'desconhecido'
    
    def criar_estrategia_sequencia(self, nome, sequencia_cores, apostar_em, confianca, descricao=""):
        """
        Cria estratégia baseada em sequência de cores
        
        Args:
            nome: Nome da estratégia
            sequencia_cores: Lista de cores ['vermelho', 'preto', 'vermelho']
            apostar_em: Cor para apostar ('vermelho' ou 'preto')
            confianca: Nível de confiança (1-100)
            descricao: Descrição da estratégia
        """
        estrategia = {
            'id': len(self.estrategias_customizadas) + 1,
            'nome': nome,
            'tipo': 'sequencia_cores',
            'sequencia_cores': sequencia_cores,
            'apostar_em': apostar_em,
            'confianca': max(1, min(100, confianca)),
            'descricao': descricao,
            'ativa': True,
            'acertos': 0,
            'tentativas': 0
        }
        
        self.estrategias_customizadas.append(estrategia)
        return estrategia['id']
    
    def criar_estrategia_numero_especifico(self, nome, numero_gatilho, pedras_esperar, apostar_em, confianca, descricao=""):
        """
        Cria estratégia baseada em número específico (como as estratégias do 6 e 7)
        
        Args:
            nome: Nome da estratégia
            numero_gatilho: Número que dispara a estratégia (0-14)
            pedras_esperar: Quantas pedras esperar após o número
            apostar_em: Cor para apostar ('vermelho' ou 'preto')
            confianca: Nível de confiança (1-100)
            descricao: Descrição da estratégia
        """
        estrategia = {
            'id': len(self.estrategias_customizadas) + 1,
            'nome': nome,
            'tipo': 'numero_especifico',
            'numero_gatilho': numero_gatilho,
            'pedras_esperar': pedras_esperar,
            'apostar_em': apostar_em,
            'confianca': max(1, min(100, confianca)),
            'descricao': descricao,
            'ativa': True,
            'acertos': 0,
            'tentativas': 0
        }
        
        self.estrategias_customizadas.append(estrategia)
        return estrategia['id']
    
    def criar_estrategia_contagem(self, nome, cor_contar, quantidade_minima, apostar_em, confianca, janela_analise=10, descricao=""):
        """
        Cria estratégia baseada em contagem de cores
        
        Args:
            nome: Nome da estratégia
            cor_contar: Cor para contar ('vermelho', 'preto' ou 'branco')
            quantidade_minima: Quantidade mínima para disparar sinal
            apostar_em: Cor para apostar ('vermelho' ou 'preto')
            confianca: Nível de confiança (1-100)
            janela_analise: Quantos resultados analisar
            descricao: Descrição da estratégia
        """
        estrategia = {
            'id': len(self.estrategias_customizadas) + 1,
            'nome': nome,
            'tipo': 'contagem',
            'cor_contar': cor_contar,
            'quantidade_minima': quantidade_minima,
            'apostar_em': apostar_em,
            'confianca': max(1, min(100, confianca)),
            'janela_analise': janela_analise,
            'descricao': descricao,
            'ativa': True,
            'acertos': 0,
            'tentativas': 0
        }
        
        self.estrategias_customizadas.append(estrategia)
        return estrategia['id']
    
    def analisar_estrategia_sequencia(self, estrategia):
        """Analisa estratégia de sequência de cores"""
        sequencia = estrategia['sequencia_cores']
        tamanho_sequencia = len(sequencia)
        
        if len(self.historico) < tamanho_sequencia:
            return None
        
        # Converter últimos resultados para cores
        cores_recentes = []
        for numero in self.historico[-tamanho_sequencia:]:
            cores_recentes.append(self.cor_do_numero(numero))
        
        # Verificar se a sequência bate
        if cores_recentes == sequencia:
            return {
                'sinal': estrategia['apostar_em'],
                'confianca': estrategia['confianca'],
                'estrategia': f"{estrategia['nome']} (Personalizada)",
                'protecao': 'branco',
                'estrategia_id': estrategia['id']
            }
        
        return None
    
    def analisar_estrategia_numero_especifico(self, estrategia):
        """Analisa estratégia de número específico"""
        numero_gatilho = estrategia['numero_gatilho']
        pedras_esperar = estrategia['pedras_esperar']
        
        if len(self.historico) < pedras_esperar + 1:
            return None
        
        # Procurar pelo número gatilho
        for i in range(len(self.historico) - pedras_esperar, len(self.historico)):
            if i >= 0 and self.historico[i] == numero_gatilho:
                pedras_apos_gatilho = len(self.historico) - i - 1
                
                if pedras_apos_gatilho == pedras_esperar:
                    return {
                        'sinal': estrategia['apostar_em'],
                        'confianca': estrategia['confianca'],
                        'estrategia': f"{estrategia['nome']} (Personalizada)",
                        'protecao': 'branco',
                        'estrategia_id': estrategia['id']
                    }
        
        return None
    
    def analisar_estrategia_contagem(self, estrategia):
        """Analisa estratégia de contagem"""
        cor_contar = estrategia['cor_contar']
        quantidade_minima = estrategia['quantidade_minima']
        janela = estrategia['janela_analise']
        
        if len(self.historico) < janela:
            return None
        
        # Contar ocorrências da cor na janela
        cores_recentes = []
        for numero in self.historico[-janela:]:
            cores_recentes.append(self.cor_do_numero(numero))
        
        contagem = cores_recentes.count(cor_contar)
        
        if contagem >= quantidade_minima:
            return {
                'sinal': estrategia['apostar_em'],
                'confianca': estrategia['confianca'],
                'estrategia': f"{estrategia['nome']} (Personalizada - {contagem}/{janela} {cor_contar})",
                'protecao': 'branco',
                'estrategia_id': estrategia['id']
            }
        
        return None
    
    def analisar_estrategias_personalizadas(self):
        """Analisa todas as estratégias personalizadas ativas"""
        sinais_encontrados = []
        
        for estrategia in self.estrategias_customizadas:
            if not estrategia['ativa']:
                continue
            
            sinal = None
            
            if estrategia['tipo'] == 'sequencia_cores':
                sinal = self.analisar_estrategia_sequencia(estrategia)
            elif estrategia['tipo'] == 'numero_especifico':
                sinal = self.analisar_estrategia_numero_especifico(estrategia)
            elif estrategia['tipo'] == 'contagem':
                sinal = self.analisar_estrategia_contagem(estrategia)
            
            if sinal:
                sinais_encontrados.append(sinal)
        
        # Retornar sinal com maior confiança
        if sinais_encontrados:
            return max(sinais_encontrados, key=lambda x: x['confianca'])
        
        return None
    
    def atualizar_estatisticas(self, estrategia_id, acertou):
        """Atualiza estatísticas de uma estratégia"""
        for estrategia in self.estrategias_customizadas:
            if estrategia['id'] == estrategia_id:
                estrategia['tentativas'] += 1
                if acertou:
                    estrategia['acertos'] += 1
                break
    
    def obter_estrategias(self):
        """Retorna lista de todas as estratégias"""
        estrategias_com_stats = []
        
        for estrategia in self.estrategias_customizadas:
            estrategia_copy = estrategia.copy()
            
            # Calcular taxa de acerto
            if estrategia['tentativas'] > 0:
                estrategia_copy['taxa_acerto'] = (estrategia['acertos'] / estrategia['tentativas']) * 100
            else:
                estrategia_copy['taxa_acerto'] = 0
            
            estrategias_com_stats.append(estrategia_copy)
        
        return estrategias_com_stats
    
    def remover_estrategia(self, estrategia_id):
        """Remove uma estratégia"""
        self.estrategias_customizadas = [e for e in self.estrategias_customizadas if e['id'] != estrategia_id]
    
    def ativar_desativar_estrategia(self, estrategia_id, ativa):
        """Ativa ou desativa uma estratégia"""
        for estrategia in self.estrategias_customizadas:
            if estrategia['id'] == estrategia_id:
                estrategia['ativa'] = ativa
                break

# ANALISADOR COMPLETO COM ESTRATÉGIAS PERSONALIZADAS
class AnalisadorCompleto:
    """
    Analisador que combina estratégias padrão e personalizadas
    """
    
    def __init__(self, historico):
        self.estrategias_padrao = EstrategiasDouble()
        self.estrategias_personalizadas = EstrategiasPersonalizadas()
        
        # Adicionar histórico a ambos os sistemas
        for resultado in historico:
            self.estrategias_padrao.adicionar_resultado(resultado)
            self.estrategias_personalizadas.adicionar_resultado(resultado)
    
    def analisar_padroes(self):
        """
        Analisa tanto estratégias padrão quanto personalizadas
        Prioriza estratégias personalizadas se tiverem maior confiança
        """
        # Analisar estratégias personalizadas primeiro
        sinal_personalizado = self.estrategias_personalizadas.analisar_estrategias_personalizadas()
        
        # Analisar estratégias padrão
        sinal_padrao = self.estrategias_padrao.analisar_padroes()
        
        # Decidir qual sinal usar
        if sinal_personalizado and sinal_padrao:
            # Usar o de maior confiança
            if sinal_personalizado['confianca'] >= sinal_padrao['confianca']:
                return sinal_personalizado
            else:
                return sinal_padrao
        elif sinal_personalizado:
            return sinal_personalizado
        elif sinal_padrao:
            return sinal_padrao
        
        return None
    
    def obter_estrategias_personalizadas(self):
        """Retorna estratégias personalizadas"""
        return self.estrategias_personalizadas.obter_estrategias()
    
    def adicionar_estrategia_personalizada(self, tipo, **kwargs):
        """Adiciona nova estratégia personalizada"""
        if tipo == 'sequencia':
            return self.estrategias_personalizadas.criar_estrategia_sequencia(**kwargs)
        elif tipo == 'numero':
            return self.estrategias_personalizadas.criar_estrategia_numero_especifico(**kwargs)
        elif tipo == 'contagem':
            return self.estrategias_personalizadas.criar_estrategia_contagem(**kwargs)
        
        return None 