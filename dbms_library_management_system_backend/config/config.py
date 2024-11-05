import os

class Config_:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password/9@localhost/library_management_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True