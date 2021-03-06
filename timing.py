import time
import math
#The two lines above import functions within python to use simple math and the clock
def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time ; ", end - begin)
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    math.factorial(num)

factorial(10)
'''This function finds the difference in the start and end time it took to run theh function'''
