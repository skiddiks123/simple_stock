from flask import abort, flash, redirect, render_template, url_for, jsonify, request
from flask_login import current_user, login_required

from app.models.user import User
from flask import Blueprint

admin = Blueprint('admin', __name__,  template_folder='templates', url_prefix='/admin')

@admin.route('/list_users/')
@login_required
def list_users():
    users = User.query.all()
    print(users)
    return render_template('admin/users.html',
                           users=users, title='Пользователи')


@admin.route('/signup/', methods=['GET', 'POST'])
@login_required
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

@admin.route('/delete_user/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
   
    print(id)
    user = User.query.filter_by(id = id).first()
    print(user)
    if request.method == 'GET':
        redirect(url_for('users') + '#myModal')

    return jsonify(status='ok')

