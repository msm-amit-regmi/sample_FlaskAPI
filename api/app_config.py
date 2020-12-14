import os


def host() -> str:
    return os.getenv("APP_ADDRESS", "127.0.0.1")
    #return os.getenv("APP_ADDRESS", "3.17.189.79")


def port() -> str:
    return os.getenv("APP_PORT", 8000)
