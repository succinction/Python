import threading
from threading import Timer
from itertools import count
import itertools


def funct(*args, **kwargs):
    print("CALLED {}".format(count()))
    print("CALLED {}".format(itertools.count().__next__()))


args, kwargs = 1, [0, 1]
t = Timer(0.2, funct, None, None)
tr = Timer()
t.start()

threading.Event()
