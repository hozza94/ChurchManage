from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, IntegerField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

from _datetime import datetime


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.'), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.')])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.')])


class MemberCreateForm(FlaskForm):
    memberName = StringField('이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(max=25)])
    memberAge = IntegerField('나이', validators=[DataRequired('나이는 필수 입력 항목입니다.')])
    memberSex = StringField('성별', validators=[DataRequired('성별은 필수 입력 항목입니다.')])
    memberBirthday = DateField('생년월일', validators=[])
    memberContact1 = StringField('연락처 1', validators=[])
    memberContact2 = StringField('연락처 2', validators=[])
    memberContact3 = StringField('연락처 3', validators=[])
    memberAddress = StringField('주소', validators=[])
    memberJob = StringField('직업', validators=[])
    memberEmail = StringField('이메일', validators=[])
    memberBaptism = StringField('침례 여부', validators=[DataRequired('침례여부는 필수 입력 항목입니다.')])
    memberBaptismDay = DateField('침례일', validators=[])
    memberMarriage = StringField('결혼 여부', validators=[DataRequired('결혼여부는 필수 입력 항목입니다.')])
    memberPrevChurch = StringField('이전 교회', validators=[])
    #
    # 2021-07-09 00:00:00.0 타입 조심
    memberCreate_date = DateTimeField('사용자이름', validators=[])
    memberModify_date = DateTimeField('사용자이름', validators=[])
