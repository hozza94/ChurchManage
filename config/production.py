from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'churchm.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'@w\xd4\x97,)\xd0\xa3\xaa\xea\x8d;&\xdd\x83\xe5'
