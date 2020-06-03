from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return "working in progress to serve NLP Machine learning models"

@app.route('/text', methods=['GET', 'POST'])
def text():
    return render_template('form.html',form=form)



if __name__ == '__main__':
    app.run()

