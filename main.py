from data.User import User
from flask import Flask, render_template
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
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть или ваш пароль не подходит")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/main')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(port=8079, host='127.0.0.1')
    db_session.global_init("db/users.db")
