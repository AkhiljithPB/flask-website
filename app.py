from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

  return '<h1><center>FlaskApplication - Version - 1.7 </center></h1>'

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=5000)
