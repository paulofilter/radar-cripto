# Radar Cripto App - Pacote para Deploy Externo

Este diretório contém todos os arquivos necessários para implantar o Radar Cripto App em uma plataforma externa como Replit, Vercel ou similar.

## Estrutura de Arquivos

- `app.py` - Aplicativo Flask principal
- `requirements.txt` - Dependências Python necessárias
- `Procfile` - Configuração para plataformas como Heroku
- `refined_signals.json` - Dados de exemplo para demonstração
- `scoring_config.json` - Configuração do sistema de pontuação
- `templates/` - Diretório com templates HTML
- `static/` - Diretório com arquivos CSS e JavaScript

## Instruções de Deploy

### Para Replit

1. Crie um novo Repl com o template Python
2. Faça upload de todos os arquivos deste diretório
3. No arquivo `.replit`, configure o comando de execução para `python app.py`
4. Clique em "Run" para iniciar o aplicativo

### Para Vercel

1. Crie um novo projeto no Vercel
2. Conecte ao repositório Git contendo estes arquivos
3. Configure o comando de build para `pip install -r requirements.txt`
4. Configure o comando de execução para `python app.py`
5. Deploy o aplicativo

### Para Render

1. Crie um novo Web Service no Render
2. Conecte ao repositório Git contendo estes arquivos
3. Selecione "Python" como ambiente
4. Configure o comando de build para `pip install -r requirements.txt`
5. Configure o comando de inicialização para `gunicorn app:app`
6. Deploy o aplicativo

## Configuração

O aplicativo está configurado para usar dados de exemplo contidos em `refined_signals.json`. Para conectar a fontes de dados reais (como Binance ou CoinGecko), modifique o arquivo `app.py` conforme necessário.

## Personalização

- Modifique `templates/index.html` para ajustar a interface do usuário
- Edite `static/css/style.css` para personalizar o estilo visual
- Atualize `static/js/app.js` para modificar o comportamento do frontend

## Contato

Para suporte ou dúvidas, entre em contato com o desenvolvedor.
