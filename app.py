from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = '783hhiuy73872bbdbba0989sasd'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url-shortener', methods=['GET', 'POST'])
def url_shortener():
    if request.method == 'POST':
        urls = {}
        
        file_name = 'urls.json'
        code = request.form['code']
        if os.path.exists(file_name):
            with open(file_name) as urls_file:
                urls = json.load(urls_file)

        if code in urls.keys():
            flash('Your shorten code has been sent before')
            return redirect(url_for('home'))
        
        if 'url' in urls.keys():
            urls[code] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = code + secure_filename(f.filename)
            f.save('/Users/mac/Desktop/work/python-code/flask-pyDev/' + full_name)
            urls[code] = {'file': full_name}

        with open(file_name, 'w') as url_file:
            json.dump(urls, url_file)
       

        return render_template('url-shortener.html', code=code)
    else:
        return redirect(url_for('home'))
