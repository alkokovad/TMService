from data.User import User
from flask import Flask, render_template, request
from forms.registerform import RegisterForm
from werkzeug.utils import redirect

from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nazvanie_comandi'


@app.route('/map')
def show_map():
    return render_template('map.html')


@app.route('/onedot/')
def show_onedot_map():
    return render_template('mapOneDot.html')


@app.route('/main')
def main_page():
    return render_template('base.html')


@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/main')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(port=8079, host='127.0.0.1')
    db_session.global_init("db/users.db")
