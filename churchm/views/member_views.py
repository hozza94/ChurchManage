from flask import Blueprint, render_template, redirect, url_for, request, g, flash

from ..forms import MemberCreateForm
from churchm.models import Member
from churchm import db
from churchm.views.auth_views import login_required
from datetime import datetime

bp = Blueprint('member', __name__, url_prefix='/member')


# 교인 리스트
@bp.route('/list/')
@login_required
def _list():
    member_list = Member.query.order_by(Member.create_date.desc())
    return render_template('member/member_list.html', member_list=member_list)


# 교인 상세 조회
@bp.route('/detail/<int:member_id>/')
@login_required
def detail(member_id):
    form = MemberCreateForm()
    member = Member.query.get_or_404(member_id)
    return render_template('member/member_detail.html', member=member, form=form)


# 교인 정보 수정
@bp.route('/modify/<int:member_id>/', methods=('GET', 'POST'))
@login_required
def modify(member_id):
    member = Member.query.get_or_404(member_id)
    if g.user.grade != 'manager':
        flash('수정권한이 없습니다.')
        return redirect(url_for('member.detail', member_id=member_id))

    if request.method == 'POST':
        form = MemberCreateForm()
        if form.validate_on_submit():
            form.populate_obj(member)
            member.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('member.detail', member_id=member_id))
    else:
        form = MemberCreateForm(obj=member)

    return render_template('member/member_modify.html', form=form, member=member)


# 교인 정보 삭제
@bp.route('/delete/<int:member_id>/')
@login_required
def delete(member_id):
    member = Member.query.get_or_404(member_id)
    if g.user.grade != "manager":
        print("접근권한 없음")
        print(g.user.grade)
        flash('삭제권한이 없습니다')
        return redirect(url_for('member.detail', member_id=member_id))
    db.session.delete(member)
    db.session.commit()
    print("commit ok")
    return redirect(url_for('member._list'))
