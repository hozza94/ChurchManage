from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


# 인삿말
@bp.route('/hello')
def hello():
    return render_template('index.html')


# 기본 페이지
@bp.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('main.hello'))