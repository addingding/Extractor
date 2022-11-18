#! /usr/bin/python3
from ecosys import *

logger.info(f"start {datetime.datetime.now()}")

if __name__ == "__main__":
    from app.scenes import start
    try:
        start()
    except Exception as e:
        logger.critical(e)

logger.info(f"end {datetime.datetime.now()}")
