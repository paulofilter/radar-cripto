
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('refined_signals.json', 'r', encoding='utf-8') as f:
        signals = json.load(f)
    return render_template('index.html', signals=signals)
