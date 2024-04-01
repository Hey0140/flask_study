import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'app/app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev" #유추하기 쉬운 문자열 절대 안됨