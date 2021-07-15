# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)



# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    data = {
        'user':{'first_name':'Derek','last_name':'Stampone'}
    }
    return render_template('index.html', data=data )

@app.route('/secret')
def secret():
    return "<h1>you found a secret!</h1>"

@app.route('/sendNickname', methods=['GET','POST'])
def recieve_nickname():
    if request.method == 'POST':
        form = request.form
        nickname = form['nickname']
        data = {
            'nickname':nickname
        }
        return render_template('results.html',data=data)
    else:
        return 'I received a GET request'
