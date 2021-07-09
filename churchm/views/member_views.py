from flask import Blueprint, render_template

from churchm.models import Member

from churchm.views.auth_views import login_required

bp = Blueprint('member', __name__, url_prefix='/member')


# 교인 리스트
@bp.route('/list/')
@login_required
def _list():
    member_list = Member.query.order_by(Member.create_date.desc())
    return render_template('member/member_list.html', member_list=member_list)


# 교인 개인 조회
@bp.route('/detail/<int:member_id>/')
@login_required
def detail(member_id):
    member = Member.query.get_or_404(member_id)
    return render_template('member/member_detail.html', member=member)


# 교인 등록
@bp.route('/create/')
@login_required
def create(member_id):
    member = Member.query.get_or_404(member_id)
    return render_template('member/member_detail.html', member=member)


# 교인 삭제