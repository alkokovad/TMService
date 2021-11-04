from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from forms.registration_form import RegisterForm

app = Flask(__name__)


def main():
    db_session.global_init("db/usersandproblems.db")
    app.run(host='localhost', port=5000)

    def __repr__(self):
        return ' '.join([self.__class__.__main__,
                         str(self.id),
                         self.name,
                         self.email])


@app.route('/main')
def main_page():
    return render_template('base.html')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
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
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
