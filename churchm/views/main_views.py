from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


# 인삿말
@bp.route('/hello')
def hello():
    return 'hi 방가방가'


# 기본 페이지
@bp.route('/')
def index():
    return redirect(url_for('member._list'))
