from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return " Working in progress to serve NLP machine learning models"

if __name__ == '__main__':
    app.run(debug=True)






