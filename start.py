#! /usr/bin/python3
from ecosys import *
logging.start()
print("start",datetime.datetime.now())

if __name__ == "__main__":
    from app.scenes import start
    try:
        start()
    except Exception as e:
        print(e)

print("end",datetime.datetime.now())
logging.release()
