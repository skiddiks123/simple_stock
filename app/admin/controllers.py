from flask import abort, flash, redirect, render_template, url_for, jsonify, request, make_response
from flask_login import current_user, login_required
from app.models.user import User
from flask import Blueprint
from app import db
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
            newuser = User(form.uname.data, form.lname.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
        session['email'] = newuser.email
        return redirect(url_for('home.index'))
    elif request.method == 'GET':
        return render_template("modals/add_user.html", form=form)

@admin.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
    if request.method == 'POST':
        try:
            user_id = request.json['userid']
            user = User.query.filter(User.id==user_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
            return make_response(jsonify( { 'status': 'ok', 'msg': 'User has been removed.' } ), 200)
        except:
            print ('error')
            return make_response(jsonify( { 'status': 'error', 'msg': 'There is something wrong, please contact Administrator.' } ), 400)

@admin.route('/check_email', methods=['POST'])
@login_required
def check_email():
    if request.method == 'POST':
        try:
            print(request.json['email'])
            user = User.query.filter(User.id==user_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
            return make_response(jsonify( { 'status': 'ok', 'msg': 'User has been removed.' } ), 200)
        except:
            print ('error')
            return make_response(jsonify( { 'status': 'error', 'msg': 'There is something wrong, please contact Administrator.' } ), 400)