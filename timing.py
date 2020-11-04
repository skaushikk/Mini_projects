# python3
import atexit
from time import time, strftime, localtime, sleep
from datetime import timedelta

def log(elapsed=None):
    print()
    if elapsed:
        print("[Process Finished in {:.2f} ms]".format(elapsed))
    # print(line)
    print()


def endlog():
    end = time()
    # sleep(1)
    elapsed = (end - start)*1000
    log(elapsed)


start = time()
atexit.register(endlog)
print()
