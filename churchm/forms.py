from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateTimeField, IntegerField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

from _datetime import datetime


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.'), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.')])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.')])


class MemberCreateForm(FlaskForm):
    memberName = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberAge = IntegerField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberSex = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberBirthday = DateField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberContact1 = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberContact2 = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberContact3 = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberAddress = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberJob = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberEmail = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberBaptism = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberBaptismDay = DateField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberMarriage = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberPrevChurch = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    #
    # 2021-07-09 00:00:00.0 타입 조심
    memberCreate_date = DateTimeField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    memberModify_date = DateTimeField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
