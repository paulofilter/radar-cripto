
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('refined_signals.json', 'r', encoding='utf-8') as f:
        signals = json.load(f)

    classification = request.args.get('classification')
    direction = request.args.get('direction')
    symbol = request.args.get('symbol')

    filtered = signals
    if classification:
        filtered = [s for s in filtered if s['classification'].lower() == classification.lower()]
    if direction:
        filtered = [s for s in filtered if s['direction'].lower() == direction.lower()]
    if symbol:
        filtered = [s for s in filtered if symbol.upper() in s['symbol'].upper()]

    return render_template('index.html', signals=filtered)
