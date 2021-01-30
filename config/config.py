import os


class Config(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(os.getenv(
      'DB_USER'), os.getenv('DB_PASS'), os.getenv('DB_HOST'), os.getenv('DB_POST'), os.getenv('DB_NAME'))
  SQLALCHEMY_ECHO = False
  JWT_SECRET_KEY = 'JWT-SECRET'
  SECRET_KEY = 'SECRET-KEY'
  SECURITY_PASSWORD_SALT = 'SECRET-KEY-PASSWORD'


class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(os.getenv(
      'DB_USER'), os.getenv('DB_PASS'), os.getenv('DB_HOST'), os.getenv('DB_POST'), os.getenv('DB_NAME'))
  SQLALCHEMY_ECHO = False
  JWT_SECRET_KEY = 'JWT-SECRET'
  SECRET_KEY = 'SECRET-KEY'
  SECURITY_PASSWORD_SALT = 'SECRET-KEY-PASSWORD'
