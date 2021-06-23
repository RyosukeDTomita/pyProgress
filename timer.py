##########################################################################
# Name: timer.py
# calcurate program runtime
#
# Usage:
#```python3
#from timer import timer
#start = timer()
#```
# Author: Ryosuke Tomita
# Date: 2021/06/23
##########################################################################
import time
class timer:
    def __init__(self):
        self.start = time.time()
        return None
    def end(self):
        self.end = time.time()
        runTime = self.end - self.start
        print("runTime is",runTime,"seconds")
        return runTime
    def __del__(self):
        self.end = time.time()
        runTime = self.end - self.start
        print("runTime is",runTime,"seconds")
        return runTime
