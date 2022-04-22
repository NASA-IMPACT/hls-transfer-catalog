import os


class BaseConfig:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME", "tempdb")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_TYPE = os.getenv("DB_TYPE", "postgresql")


class LocalConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


CONFIG_BY_ENV = dict(local=LocalConfig, testing=TestingConfig, prod=ProdConfig)
