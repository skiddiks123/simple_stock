from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app.mod_auth.forms import LoginForm, SignupForm
from app.models.user import User
from app import db

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.pwdhash, form.password.data):
            session['user_id'] = user.id
            flash('Добро пожаловать %s' % user.nickname)
            return redirect(url_for('home.index'))
        flash('Не верный логин или пароль', 'error-message')
    return render_template("auth/signin.html", form=form)

@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("auth/signup.html", form=form)
        else:
            newuser = User(form.nickname.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
        session['email'] = newuser.email
        return redirect(url_for('auth.profile'))
    elif request.method == 'GET':
        return render_template("auth/signup.html", form=form)