class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 's1N#yJkJxrwYg+p'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@localhost/login-chefsito"
    FLASK_SECRET = SECRET_KEY
