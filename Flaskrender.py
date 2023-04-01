from distutils.log import debug
from fileinput import filename
from flask import *
from flask import Blueprint, render_template,redirect
from app import *

app = Flask(__name__,static_folder='static')
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/demo')
def demo():
    start()
    return 

if __name__ == '__main__':
    app.run(debug=True)
