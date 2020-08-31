class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql+mysqldb://urbanedg_mem_app:+VF@T(HH{k~X@72.52.161.232:3306/urbanedg_mem_application'
	
class DevelopmentConfig(Config):
    DEBUG = True

class SECRET_KEY(Config):
    SECRET_KEY = '5678906567890543346789976565'