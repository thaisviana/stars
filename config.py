import os
import dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))


class Config(object):
    MONGO_URI = os.environ.get('MONGODB_URI')
    DEBUG = False
    TESTING = False
    DATABASE_URI = MONGO_URI
    SECRET_KEY = os.environ.get('SECRET_KEY', '53cr3t_k3y')
    CORS_HEADERS= 'Content-Type'


class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('MONGODB_URI')
