from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "working in progress to serve NLP Machine learning models"

@app.route('/text')
def text():
    return "create the webform "



if __name__ == '__main__':
    app.run()

