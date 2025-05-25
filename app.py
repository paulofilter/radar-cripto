#!/usr/bin/env python3
"""
Implementação da API de varredura personalizada para o Radar Cripto App.
Este módulo processa os filtros selecionados pelo usuário e retorna sinais em tempo real.
"""

import os
import json
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory
import pandas as pd
import numpy as np

# Configurações
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

# Criar diretório de dados se não existir
os.makedirs(DATA_DIR, exist_ok=True)

# Inicializar Flask
app = Flask(__name__, 
            static_folder=STATIC_DIR,
            template_folder=TEMPLATES_DIR)

# Carregar dados de exemplo para desenvolvimento
def load_sample_signals():
    """Carrega sinais de exemplo do arquivo JSON."""
    try:
        with open('refined_signals.json', 'r') as f:
            data = json.load(f)
            return data.get('signals', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar sinais de exemplo: {e}")
        return []

# Função para aplicar filtros aos sinais
def apply_filters(signals, filters):
    """Aplica filtros aos sinais conforme critérios do usuário."""
    filtered_signals = signals.copy()
    
    # Filtrar por classificação
    if 'classification' in filters and filters['classification']:
        classifications = filters['classification'].split(',')
        filtered_signals = [s for s in filtered_signals if s['classification'] in classifications]
    
    # Filtrar por direção
    if 'direction' in filters and filters['direction']:
        directions = filters['direction'].split(',')
        filtered_signals = [s for s in filtered_signals if s['direction'] in directions]
    
    # Filtrar por símbolo
    if 'symbol' in filters and filters['symbol']:
        symbol = filters['symbol'].upper()
        filtered_signals = [s for s in filtered_signals if symbol in s['symbol']]
    
    # Filtrar por timeframe
    if 'timeframe' in filters and filters['timeframe']:
        timeframes = filters['timeframe'].split(',')
        filtered_signals = [s for s in filtered_signals if s['timeframe'] in timeframes]
    
    # Filtrar por score mínimo
    if 'min_score' in filters and filters['min_score']:
        min_score = int(filters['min_score'])
        # Converter score interno (0-100) para simplificado (0-10)
        filtered_signals = [s for s in filtered_signals if convert_score_to_simplified(s['score']) >= min_score]
    
    # Filtrar por indicadores
    if 'indicators' in filters and filters['indicators']:
        indicators = filters['indicators'].split(',')
        filtered_signals = [
            s for s in filtered_signals 
            if any(indicator in s['signals'] for indicator in indicators)
        ]
    
    return filtered_signals

# Função para converter score interno (0-100) para simplificado (0-10)
def convert_score_to_simplified(score):
    """Converte score interno (0-100) para score simplificado (0-10)."""
    if score >= 90: return 10
    if score >= 80: return 9
    if score >= 70: return 8
    if score >= 60: return 7
    if score >= 50: return 6
    # Abaixo de 50, arredondar proporcionalmente
    return round(score / 10)

# Rotas da API
@app.route('/')
def index():
    """Renderiza a página principal."""
    return render_template('index.html')

@app.route('/api/signals')
def get_signals():
    """Retorna sinais filtrados conforme critérios do usuário."""
    # Obter parâmetros de filtro da requisição
    filters = {
        'classification': request.args.get('classification', ''),
        'direction': request.args.get('direction', ''),
        'symbol': request.args.get('symbol', ''),
        'timeframe': request.args.get('timeframe', ''),
        'min_score': request.args.get('min_score', ''),
        'indicators': request.args.get('indicators', '')
    }
    
    # Carregar sinais (em produção, isso viria do banco de dados ou API em tempo real)
    signals = load_sample_signals()
    
    # Aplicar filtros
    filtered_signals = apply_filters(signals, filters)
    
    return jsonify(filtered_signals)

@app.route('/api/config')
def get_config():
    """Retorna configurações do aplicativo."""
    config = {
        'timeframes': ['M15', 'H1', 'H4', 'D1'],
        'indicators': ['MM50', 'MM100', 'MM200', 'RSI', 'OB', 'BOS', 'CHoCH', 'VOLUME'],
        'classifications': ['PREMIUM', 'FORTE', 'MODERADO', 'FRACO'],
        'directions': ['bullish', 'bearish']
    }
    return jsonify(config)

@app.route('/api/stats')
def get_stats():
    """Retorna estatísticas de monitoramento."""
    stats = get_monitoring_stats()
    return jsonify(stats)

@app.route('/historico')
def history():
    """Renderiza a página de histórico."""
    return render_template('history.html')

@app.route('/configuracoes')
def settings():
    """Renderiza a página de configurações."""
    return render_template('settings.html')

# Iniciar servidor
if __name__ == '__main__':
    
    
    # Iniciar servidor Flask
    app.run(host='0.0.0.0', port=8080, debug=True)
