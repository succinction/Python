# import time
# starttime = time.time()
# settimeout = 1.0
# while True:
#     print("tick")
#
#
#     time.sleep(settimeout - ((time.time() - starttime) % settimeout))

    # input("Testing for concurency : enter ")

############# WORKS ######################


import sched, time
s = sched.scheduler(time.time, time.sleep)



def stuff():
    print("more stuff")
    input("now what? : ")


def do_something(sc):
    print("Doing stuff...")

    s.enter(.5, 1, do_something, (sc,))
    stuff()

    # do your stuff

s.enter(.5, 1, do_something, (s,))
s.run()




################### THESE DONT WORK #######################

# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def print_time(a='default'):
#     print("From print_time", time.time(), a)
#
# def print_some_times():
#     print(time.time())
#     s.enter(3, 1, print_time)
#     s.enter(2, 2, print_time, argument=('positional',))
#     s.enter(1, 1, print_time, kwargs={'a': 'keyword'})
#     s.run()
#     print(time.time())
# print_some_times()
#
# '''
# 930343690.257
# From print_time 930343695.274 positional
# From print_time 930343695.275 keyword
# From print_time 930343700.273 default
# 930343700.276
# '''
#



# import threading
#
# def printit():
#   threading.Timer(1.0, printit).start()
#   print ("Hello, World!")
#
# printit()

# continue with the rest of your code




# import time
# starttime=time.time()
# while True:
#   print("tick")
#   time.sleep(2.0 - ((time.time() - starttime) % 60.0))




