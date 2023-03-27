from distutils.log import debug
from fileinput import filename
from flask import *  
app = Flask(__name__)  
  
@app.route('/')  
def main():  
    return render_template("index.html")  
  
if __name__ == '__main__':  
    app.run(debug=True)