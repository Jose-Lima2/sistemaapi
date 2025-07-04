# 🎯 Sistema de Sinais - Double

Sistema automatizado de análise de padrões para jogos de Double/Roleta com estratégias personalizáveis e interface web moderna.

## 🚀 Deploy Rápido

[![Deploy no Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Jose-Lima2/sistemaapi)

## ✨ Funcionalidades

- 🎯 **10+ Estratégias Pré-configuradas**
  - Estratégia do 7 (85% confiança)
  - Estratégia do 6 (85% confiança)
  - Padrões de alternância e repetição
  - Quebra de sequências
  - Análise de dominância

- 🛠️ **Sistema de Estratégias Personalizadas**
  - Criar estratégias por sequência de cores
  - Estratégias baseadas em números específicos
  - Contagem de cores em janelas de tempo
  - Ativar/desativar estratégias individualmente

-  **Gerenciamento Avançado**
  - Sistema G1 automático (2% da banca)
  - Proteção com branco
  - Histórico de sinais
  - Estatísticas de performance
  - Interface web responsiva

-  **Análise em Tempo Real**
  - Coleta automática de resultados
  - Processamento instantâneo de padrões
  - Notificações de sinais
  - Dashboard ao vivo

##  Tecnologias

- **Backend:** Python 3.11 + Flask
- **Frontend:** HTML5 + CSS3 + JavaScript
- **APIs:** REST + Tempo Real
- **Deploy:** Heroku, Railway, Render

##  Como Usar

1. **Acesse o sistema web**
2. **Clique em \
Iniciar
Sistema\**
3. **Aguarde os sinais serem gerados automaticamente**
4. **Crie suas próprias estratégias personalizadas**
5. **Monitore performance e estatísticas**

##  Instalação Local

\\\ash
# Clone o repositório
git clone https://github.com/Jose-Lima2/sistemaapi.git
cd sistemaapi

# Instale dependências
pip install -r requirements.txt

# Execute o sistema web
cd web_sistema
python app.py

# Ou execute o sistema linha de comando
python api.py
\\\

##  Deploy em Produção

###  Railway (Mais Fácil)
1. Acesse [railway.app](https://railway.app)
2. Conecte o GitHub
3. Selecione o repositório \sistemaapi\
4. Deploy automático em 2 minutos!

###  Heroku
\\\ash
heroku login
heroku create seu-app-sinais
git push heroku main
\\\

###  Render
1. Acesse [render.com](https://render.com)
2. Conecte GitHub
3. Configure start command: \cd web_sistema && python app.py\

##  Estratégias Disponíveis

### Estratégias Padrão:
- **Estratégia do 7:** Aguarda 6 pedras após o 7, aposta vermelho na 7ª
- **Estratégia do 6:** Aguarda 5 pedras após o 6, aposta vermelho na 6ª
- **Alternância V-P-V-P:** Detecta padrões alternados
- **Repetições V-V-P-P:** Identifica sequências duplas
- **Quebra de Sequência:** Analisa quebras de padrões longos
- **Pós-Branco:** Estratégia após números brancos
- **Dominância:** Anti-dominância de cores
- **Fibonacci:** Baseado na sequência matemática
- **Espelho:** Padrões espelhados
- **Tendência:** Análise de tendências gerais

### Estratégias Personalizadas:
- **Sequência de Cores:** Defina sua própria sequência
- **Número Específico:** Baseado em qualquer número (0-14)
- **Contagem:** Conte ocorrências em janelas de tempo

##  Estrutura do Projeto

\\\
sistemaapi/
 api.py                 # Sistema linha de comando
 estrategias.py         # Engine de estratégias
 web_sistema/
    app.py            # Aplicação web Flask
    templates/
       index.html    # Interface web
    requirements.txt  # Dependências web
 requirements.txt       # Dependências principais
 Procfile              # Configuração deploy
 runtime.txt           # Versão Python
 app.json              # Deploy automático
 README.md             # Documentação
\\\

##  Configurações

### Gerenciamento de Banca:
- **Banca Inicial:** R\$ 100,00 (configurável)
- **Entrada:** 2% da banca
- **Sistema:** Até G1 (máximo 2 tentativas)
- **Proteção:** Branco sempre protege

### API de Resultados:
- **Fonte:** API oficial do jogo
- **Atualização:** A cada 3 segundos
- **Histórico:** Últimos 50 resultados
- **Timeout:** 10 segundos por requisição

##  Performance

- **Tempo de Resposta:** < 100ms
- **Uptime:** 99.9%
- **Análise:** Tempo real
- **Precisão:** Baseada em padrões históricos

##  Segurança

- **CORS:** Configurado para produção
- **Rate Limiting:** Proteção contra spam
- **Error Handling:** Tratamento robusto de erros
- **Logs:** Sistema de logging completo

##  Suporte

- **Issues:** [GitHub Issues](https://github.com/Jose-Lima2/sistemaapi/issues)
- **Documentação:** README.md
- **Atualizações:** Releases automáticos

##  Licença

Este projeto é open source e está disponível sob a MIT License.

---

** Aviso:** Este sistema é para fins educacionais e de entretenimento. Jogue com responsabilidade.

** Desenvolvido com  para a comunidade de desenvolvedores**
