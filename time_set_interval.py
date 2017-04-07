
import threading

def printit():
  threading.Timer(1.0, printit).start()
  print ("Hello, World!")

printit()

# continue with the rest of your code




# import time
# starttime=time.time()
# while True:
#   print("tick")
#   time.sleep(2.0 - ((time.time() - starttime) % 60.0))