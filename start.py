#! /usr/bin/python3
from ecosys import *

logger.info("start")

if __name__ == "__main__":
    from app.scenes import start
    try:
        start()
    except Exception as e:
        logger.error(e)

logger.info("end")
