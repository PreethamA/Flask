from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return "working in progress to serve NLP Machine learning models"
'''
@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
    return render_template('form.html',form=form)

'''
@app.route('/text')
def text():
    user_agent=request.headers.get("user-agent")
    return "<p>Your browser is %s </p>" % user_agent

if __name__ == '__main__':
    app.run(debug=True)

