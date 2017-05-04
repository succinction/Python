import threading


class PrimeNumber(threading.Thread):
    prime_numbers = {}
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[number] = "None"
        PrimeNumber.lock.release()

    def run(self):
        counter = 2
        res = True
        while counter * counter < self.Number and res:
            if self.Number % counter == 0:
                print("{} is no prime number, because {} = {} * {}".format(self.Number, self.Number, counter, self.Number / counter))

                res = False
            else:
                print("{} is a prime number".format(self.Number))

            counter += 1
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[self.Number] = res
        PrimeNumber.lock.release()


threads = []
while True:
    inpt = int(input("number: "))
    if inpt < 2:
        break

    thread = PrimeNumber(inpt)
    threads += [thread]
    thread.start()

for x in threads:
    x.join()

# import threading
##
# class PrimeNumber(threading.Thread):
#     def __init__(self, number):
#         threading.Thread.__init__(self)
#         self.Number = number
#
#     def run(self):
#         counter = 2
#         while counter * counter < self.Number:
#             if self.Number % counter == 0:
#                 print("{} is no prime number, because {} = {} * {}".format(self.Number, self.Number, counter, self.Number / counter))
#                 return
#             counter += 1
#             print("{} is a prime number".format(self.Number))
#
#
# threads = []
# while True:
#     inpt = int(input("number: "))
#     if inpt < 1:
#         break
#
#     thread = PrimeNumber(inpt)
#     threads += [thread]
#     thread.start()
#
# for x in threads:
#     x.join()




# import time
# from threading import Thread
#
# def sleeper(i):
#     print("thread {} sleeps for 5 seconds".format(i))
#     time.sleep(5)
#     print("thread {} woke up".format(i))
#
# for i in range(10):
#     t = Thread(target=sleeper, args=(i,))
#     t.start()