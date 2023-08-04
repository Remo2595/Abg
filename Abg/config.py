from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True
    OWNER_ID = int(getenv("OWNER_ID", "1410593160"))
    LOGGER_ID = getenv("LOGGER_ID", " -1001596697160")
    TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
    DEV_USERS = set(int(x) for x in getenv("DEV_USERS", "1410593160").split())
    HANDLER = getenv("HANDLER", "/ ! + . $").split()


class Development(Config):
    LOGGER = True
