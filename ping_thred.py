import threading, time, random, queue

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True

def fuzz():
    if FUZZ:
        time.sleep(random.random())

###########################################################################################

counter = 0

counter_queue = queue.Queue()

def counter_manager():
    'I have EXCLUSIVE rights to update the counter variable'
    global counter

    while True:
        increment = counter_queue.get()
        fuzz()
        oldcnt = counter
        fuzz()
        counter = oldcnt + increment
        fuzz()
        print_queue.put([
            'The count is %d' % counter,
            '---------------'])
        fuzz()
        counter_queue.task_done()

t = threading.Thread(target=counter_manager)
t.daemon = True
t.start()
del t

###########################################################################################

print_queue = queue.Queue()

def print_manager():
    'I have EXCLUSIVE rights to call the "print" keyword'
    while True:
        job = print_queue.get()
        fuzz()
        for line in job:
            print(line, end='')
            fuzz()
            print()
            fuzz()
        print_queue.task_done()
        fuzz()

t = threading.Thread(target=print_manager)
t.daemon = True
t.start()
del t

###########################################################################################

def worker():
    'My job is to increment the counter and print the current count'
    counter_queue.put(1)
    fuzz()

print_queue.put(['Starting up'])
fuzz()

worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()
    fuzz()
for t in worker_threads:
    fuzz()
    t.join()

counter_queue.join()
fuzz()
print_queue.put(['Finishing up'])
fuzz()
print_queue.join()
fuzz()





# import threading, time, random
#
# ##########################################################################################
# # Fuzzing is a technique for amplifying race condition errors to make them more visible
#
# FUZZ = True
#
# def fuzz():
#     if FUZZ:
#         time.sleep(random.random())
#
# ###########################################################################################
#
# counter = 0
#
# def worker():
#     'My job is to increment the counter and print the current count'
#     global counter
#
#     fuzz()
#     oldcnt = counter
#     fuzz()
#     counter = oldcnt + 1
#     fuzz()
#     print('The count is %d' % counter, end='')
#     fuzz()
#     print()
#     fuzz()
#     print('---------------', end='')
#     fuzz()
#     print()
#     fuzz()
#
# print('Starting up')
# fuzz()
# for i in range(10):
#     threading.Thread(target=worker).start()
#     fuzz()
# print('Finishing up')
# fuzz()
#


# import threading
#
# counter = 0
#
# def worker():
#     'My job is to increment the counter and print the current count'
#     global counter
#
#     counter += 1
#     print('The count is %d' % counter)
#     print('---------------')
#
# print('Starting up')
# for i in range(10):
#     threading.Thread(target=worker).start()
# print('Finishing up')










# import queue
# import threading
# # import urllib as urllib2
# #
# # # called by each thread
# # def get_url(q, url):
# #     q.put(urllib2.open(url).read())
#
# theurls = ["http://google.com", "http://yahoo.com"]
#
# q = queue.Queue()
#
# for u in theurls:
#     t = threading.Thread(target=get_url, args = (q,u))
#     t.daemon = True
#     t.start()
#
# s = q.get()
# print(s)









# import os, re, threading
#
#
# class ip_check(threading.Thread):
#     def __init__(self, ip):
#         threading.Thread.__init__(self)
#         self.ip = ip
#         self.__successful_pings = -1
#
#     def run(self):
#         ping_out = os.popen("ping -q -c2 " + self.ip, "r")
#         while True:
#             line = ping_out.readline()
#             if not line: break
#             n_received = re.findall(received_packages, line)
#             if n_received:
#                 self.__successful_pings = int(n_received[0])
#
#     def status(self):
#         if self.__successful_pings == 0:
#             return "no response"
#         elif self.__successful_pings == 1:
#             return "alive, but 50 % package loss"
#         elif self.__successful_pings == 2:
#             return "alive"
#         else:
#             return "shouldn't occur"
#
#
# received_packages = re.compile(r"(\d) received")
#
# check_results = []
# for suffix in range(20, 22):
#     ip = "192.168.178." + str(suffix)
#     current = ip_check(ip)
#     check_results.append(current)
#     current.start()
#
# for el in check_results:
#     el.join()
#     print("Status from ", el.ip, "is", el.status())












# import os
# import re
#
# received_packages = re.compile(r"(\d) received")
# status = ("no response", "alive but losses", "alive")
#
# for suffix in range(20, 30):
#     ip = "192.168.178." + str(suffix)
#     ping_out = os.popen("ping -q -c2 " + ip, "r")
#     print("... pinging ", ip)
#     while True:
#         line = ping_out.readline()
#         if not line: break
#         n_received = received_packages.findall(line)
#         if n_received:
#             print(ip + ": " + status[int(n_received[0])])
