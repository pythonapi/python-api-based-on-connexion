import os
import connexion
from service.Mysql import Mysql

# Configs
class Config:
    SECRET_KEY = 'ADD-KEY-HERE'
    ENV = 'dev'


class DevelopmentConfig(Config):
    # General
    DEBUG = True
    # DB
    DB_HOST = ''
    DB_USER = ''
    DB_PASSWORD = ''
    DB_NAME = ''


class TestingConfig(Config):
    # General
    DEBUG = True
    # DB
    DB_HOST = ''
    DB_USER = ''
    DB_PASSWORD = ''
    DB_NAME = ''


class ProductionConfig(Config):
    # General
    DEBUG = False
    # DB
    DB_HOST = ''
    DB_USER = ''
    DB_PASSWORD = ''
    DB_NAME = ''


config_by_env = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)


# Create the connexion application instance
basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Create the db instance
db = Mysql(
    config_by_env[Config.ENV].DB_HOST,
    config_by_env[Config.ENV].DB_USER,
    config_by_env[Config.ENV].DB_PASSWORD,
    config_by_env[Config.ENV].DB_NAME
)
