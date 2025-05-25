# Radar Cripto App - Documentação Atualizada

## Visão Geral
O Radar Cripto App é uma ferramenta avançada para identificação de oportunidades de trading em criptomoedas, focada em detectar sinais baseados em médias móveis, estrutura de mercado e outros indicadores técnicos. O aplicativo funciona como um "radar" que economiza o tempo do trader, identificando automaticamente zonas de interesse nos pares de criptomoedas.

## Novas Funcionalidades Implementadas

### 1. Identificação do Timeframe nos Sinais
- Cada sinal agora exibe claramente o timeframe da análise (D1, H4, H1, M15)
- Ícones intuitivos para cada timeframe facilitam a identificação visual
- Posicionamento destacado no topo do card para rápida visualização

### 2. Design Visual Moderno
- Cards redesenhados com visual mais limpo e profissional
- Score simplificado (0-10) destacado em círculo colorido
- Código de cores para direção (verde para Bullish, vermelho para Bearish)
- Ícones para indicadores confirmados
- Layout responsivo para desktop e mobile

### 3. Monitoramento Ampliado
- Escaneamento de todos os pares USDT da Binance
- Filtro de volume mínimo para excluir moedas sem liquidez
- Contador de pares monitorados no painel principal
- Cache inteligente para otimizar requisições à API

### 4. Painel de Filtros Interativo
- Seleção múltipla de timeframes (M15, H1, H4, D1)
- Filtros por direção (Bullish/Bearish)
- Filtros por classificação (Premium, Forte, Moderado, Fraco)
- Seleção de indicadores específicos (MM50, MM100, MM200, RSI, OB, BOS, CHoCH, Volume)
- Slider para definir score mínimo (0-10)
- Campo para busca de par específico

### 5. Varredura Personalizada
- Botão "Buscar Sinais" para executar varredura com filtros selecionados
- Resultados em tempo real
- Feedback visual durante o processamento
- Persistência de preferências do usuário

## Como Usar

### Monitoramento Básico
1. Ao acessar o aplicativo, você verá imediatamente os sinais ativos classificados como Moderado ou superior
2. O contador no topo mostra quantos pares estão sendo monitorados ativamente
3. Os cards mostram informações detalhadas de cada sinal, incluindo timeframe, direção e score

### Filtros Personalizados
1. Na seção "Filtros Personalizados", selecione as opções desejadas:
   - Clique nos timeframes que deseja monitorar
   - Selecione a direção (Bullish, Bearish ou ambos)
   - Escolha as classificações de interesse
   - Selecione indicadores específicos para filtrar
   - Ajuste o score mínimo desejado
   - Opcionalmente, digite um par específico

2. Clique em "Buscar Sinais" para aplicar os filtros
3. Os resultados serão exibidos instantaneamente na seção "Sinais Detectados"

### Interpretação dos Sinais
- **Score (0-10)**: Quanto maior, mais forte é o sinal
- **Classificação**: Premium > Forte > Moderado > Fraco
- **Direção**: Bullish (alta) ou Bearish (baixa)
- **Indicadores**: Mostra quais confirmações técnicas estão presentes
- **Categorias**: Detalha a pontuação em cada componente do sinal

## Requisitos Técnicos
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conexão à internet estável
- Suporte a JavaScript habilitado

## Instalação e Deploy

### Opção 1: Deploy via Replit
1. Crie um novo Repl com o template Python
2. Faça upload de todos os arquivos deste pacote
3. No arquivo `.replit`, configure o comando de execução para `python src/web/app.py`
4. Clique em "Run" para iniciar o aplicativo

### Opção 2: Deploy via Vercel
1. Crie um novo projeto no Vercel
2. Conecte ao repositório Git contendo estes arquivos
3. Configure o comando de build para `pip install -r src/web/requirements.txt`
4. Configure o comando de execução para `python src/web/app.py`
5. Deploy o aplicativo

### Opção 3: Execução Local
1. Instale as dependências: `pip install -r src/web/requirements.txt`
2. Execute o aplicativo: `python src/web/app.py`
3. Acesse em seu navegador: `http://localhost:8080`

## Próximos Passos
- Implementação de notificações push
- Histórico de sinais com análise de desempenho
- Integração com mais exchanges
- Personalização avançada de algoritmos
- Versão mobile nativa

## Suporte
Para suporte ou dúvidas, entre em contato com o desenvolvedor.
