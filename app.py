from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/url-shortener')
def url_shortener():
    return render_template('url-shortener.html')