from time import sleep
from threading import *
class Welcome(Thread):
    def run(self):
        for i in range(5):
            print("Welcome")
            sleep(0.5)

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.8)


t1=Welcome()
t2=Hello()
t2.start()
sleep(0.2)
t1.start()
t1.join()
t2.join()
print("Hello Everyone")
            
