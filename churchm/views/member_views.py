from flask import Blueprint, render_template

from churchm.models import Member

bp = Blueprint('member', __name__, url_prefix='/member')


# 기본 페이지
@bp.route('/list/')
def _list():
    member_list = Member.query.order_by(Member.create_date.desc())
    return render_template('member/member_list.html', member_list=member_list)


# 교인 개인 조회
@bp.route('/detail/<int:member_id>/')
def detail(member_id):
    member = Member.query.get(member_id)
    return render_template('member/member_detail.html', member=member)