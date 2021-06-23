import pyprogress
from timer import timer
startcal = timer()

for i in range(0,20,1):
    print("Hello World")
    pyprogress.bar(i,19)

