import time
import threading
def square(num):
    print("Calculate square of a number ")
    for n in num:
        time.sleep(0.3)
        print("Square is : ",n*n)


def cube(num):
    print("Calculate cube of a number ")
    for n in num:
        time.sleep(0.5)
        print("Cube is : ",n*n*n)

arr=[2,3,4]

th1=threading.Thread(target=square,args=(arr,))
th2=threading.Thread(target=cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("Complete Multithreading")
