from flask import Flask, render_template, request, redirect, url_for
import json
import os.path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url-shortener', methods=['GET', 'POST'])
def url_shortener():
    if request.method == 'POST':
        urls = {}
        
        file_name = 'urls.json'
        if os.path.exists(file_name):
            with open(file_name) as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] not in urls.keys():
            urls[request.form['code']] = {'url': request.form['url']}

        with open(file_name, 'w') as url_file:
            json.dump(urls, url_file)
       

        return render_template('url-shortener.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))
