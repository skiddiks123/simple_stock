from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app.auth.forms import LoginForm, SignupForm
from app.models.user import User
from app import db
from flask_login import login_user, logout_user, login_required, current_user
from app import decorators

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signin/',methods=['GET','POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password == form.password.data:
            print(user.password)
            login_user(user, form.remember_me.data)
            session['id'] = user.id
            return redirect(request.args.get('next') or url_for('home.index'))
        flash('Invalid username or password.')
    return render_template('auth/signin.html', form=form)

@auth.route('/signup/', methods=['GET', 'POST'])
@decorators.login_required
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
        return redirect(url_for('home.index'))
    elif request.method == 'GET':
        return render_template("auth/signup.html", form=form)

@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.signin'))