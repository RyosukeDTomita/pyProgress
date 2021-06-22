##########################################################################
# Name: progress.py
#
#```
#    #bar
#    import progress
#    for i in range(0,20,1):
#        progress.bar(i,19)
#```
#
#```
#    #timer
#    import progress
#    Time = progress.timer()
#    Time.end()
#```
#
# Usage:
#
# Author: Ryosuke Tomita
# Date: 2021/06/20
##########################################################################
import shutil
import time
class bar:
    def __init__(self,nowLoopCnt,maxLoopCnt):
        self.terminal_size = shutil.get_terminal_size()
        self.terminal_columns = self.terminal_size.columns #縦
        self.terminal_lines = self.terminal_size.lines #横
        self.maxBarLength = self.terminal_columns - 10
        bar = "#"
        dot = '.'
        percent = 100 * nowLoopCnt/maxLoopCnt
        barScaled=int(self.maxBarLength*nowLoopCnt/maxLoopCnt)
        dotScaled=self.maxBarLength - barScaled
        print('\033[32m',bar*barScaled+dot*dotScaled,'\033[0m', '\033[31m',str( "%3.1f" % percent)+"%",'\033[0m')

class timer:
    def __init__(self):
        self.start = time.time()
        return None
    def end(self):
        self.end = time.time()
        runTime = self.end - self.start
        print("runTime is",runTime,"seconds")
        return runTime
