from distutils.debug import DEBUG

'''
    General configuration parent class
    '''
class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig:
    DEBUG=True

