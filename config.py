
import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&language=en&category={}&apiKey={}'

    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&sources={}&apiKey={}'

    NEWS_API_KEY = '94d343343a714ec2b5f6a024996fe7d2'
    SECRET_KEY='Flask WTF Secret Key'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}