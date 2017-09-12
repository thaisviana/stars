import os

class Config(object):
    MONGO_URI = os.environ.get('MONGOHQ_URL')
    DEBUG = False
    TESTING = False
    DATABASE_URI = MONGO_URI