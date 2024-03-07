import os

class BaseConfig:
    """BASE CONFIG"""
    TESTING = False
    #SQLALCHEMY_DATABASE_URI = False

class DevConfig(BaseConfig):
    """DEV CONFIG"""
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    app.debug = True

class StageConfig(BaseConfig):
    """STAGING/TESTING CONFIG"""
    TESTING = True

class ProdConfig(BaseConfig):
    """PROD CONFIG"""
    pass