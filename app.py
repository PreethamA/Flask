from flask import Flask


app = Flask(__name__)

@app.route('/')
def runit():
    return "working in progress to serve NLP Machine learning models"



if __name__ == '__main__':
    app.run()

