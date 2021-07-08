from churchm import db


# 사용자
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    # 보류
    # email = db.Column(db.String(120), unique=True, nullable=False)


# 교인
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(2), nullable=False)
    birthday = db.Column(db.DateTime(), nullable=True)
    contact1 = db.Column(db.String(15), nullable=True)
    contact2 = db.Column(db.String(15), nullable=True)
    contact3 = db.Column(db.String(15), nullable=True)
    address = db.Column(db.Text(), nullable=True)
    job = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    baptism = db.Column(db.String(10), nullable=False)
    baptismDay = db.Column(db.DateTime(), nullable=True)
    marriage = db.Column(db.String(5), nullable=False)
    prevChurch = db.Column(db.String(100), nullable=True)
    #
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    # 보류
    # guider = db.Column()
    # guiderContact = db.Column()
