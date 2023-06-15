from flask import Flask, render_template, request
import os

import json

from FlairNER import NER as FlairNER
from SpacyNER import NER as SpacyNER

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/spacy', methods=['GET'])
def do_spacy_ner():
    text = json.loads(request.data)
    print(text)

    return SpacyNER(text['data'])

@app.route('/flair', methods=['GET'])
def do_flair_ner():
    text = json.loads(request.data)
    print(text)

    return FlairNER(text['data'])
