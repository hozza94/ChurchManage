from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from churchm import db
from churchm.forms import UserCreateForm, UserLoginForm, MemberCreateForm
from churchm.models import User, Member

from datetime import datetime
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data, password=generate_password_hash(form.password1.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view


@bp.route('/add/', methods=('GET', 'POST'))
@login_required
def add():
    form = MemberCreateForm()

    if request.method == 'POST' and form.validate_on_submit():
        print("add access")
        member = Member(name=form.memberName.data, age=form.memberAge.data, sex=form.memberSex.data,
                        birthday=form.memberBirthday.data, contact1=form.memberContact1.data,
                        contact2=form.memberContact2.data, contact3=form.memberContact3.data,
                        address=form.memberAddress.data, job=form.memberJob.data,
                        email=form.memberEmail.data, baptism=form.memberBaptism.data,
                        marriage=form.memberMarriage.data, prevChurch=form.memberPrevChurch.data,
                        create_date=datetime.now(), modify_date=form.memberModify_date.data
                        )
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('member._list'))

    return render_template('auth/add.html', form=form)
