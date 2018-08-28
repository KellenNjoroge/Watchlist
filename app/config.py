class Config:
    """
    General configuration

    """
    pass


class ProdConfig(Config):
    """
    Production configuration child class


    Args:
    Config: The parent configuration class with general configuration settings

    """
    pass


class DevConfig(Config):
    """
    Development configuration child class

    Args:
    Config:The parent configuration class with Genera configuration settings

    """
    DEBUG = True
