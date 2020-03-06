'''
from flask import Flask, render_template, session, redirect, url_for

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, session, redirect, url_for, flash

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
        if form.validate_on_submit():
            old_name = session.get('name')
            if old_name is not None and old_name != form.name.data:
                flash('Looks like you have changed your name!')
            session['name'] = form.name.data
            form.name.data = ''
            return redirect(url_for('index'))
        return render_template('index.html',
            form = form, name = session.get('name'))
'''
from flask import Flask, request, make_response, abort, render_template
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello world </h1>'
   # return render_template("index.html")
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent
    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer', '42')
    #return response

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

@app.route('/sow/<name>')
def sow(name):
    return '<h1>Hello, %s!</h1>' % name
if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()            