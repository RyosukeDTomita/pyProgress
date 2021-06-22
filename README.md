# Pythonで進捗管理する
## Version


## Program List
- progress.py: ループがどのへんを実行しているか棒グラフで可視化する。また、実行時間の測定ができる。
- loopsample.py: progress.pyの使用例

## How to Use progress.py

```
#bar
import progress
for i in range(0,20,1):
    progress.bar(i,19)
```

```
#timer
import progress
Time = progress.timer()
Time.end()
```

### image

```
Hello World
 ..............................................................   0.0% 
Hello World
 ###...........................................................   5.3% 
Hello World
 ######........................................................   10.5% 
Hello World
 #########.....................................................   15.8% 
Hello World
 #############.................................................   21.1% 
Hello World
 ################..............................................   26.3% 
Hello World
 ###################...........................................   31.6% 
Hello World
 ######################........................................   36.8% 
Hello World
 ##########################....................................   42.1% 
Hello World
 #############################.................................   47.4% 
Hello World
 ################################..............................   52.6% 
Hello World
 ###################################...........................   57.9% 
Hello World
 #######################################.......................   63.2% 
Hello World
 ##########################################....................   68.4% 
Hello World
 #############################################.................   73.7% 
Hello World
 ################################################..............   78.9% 
Hello World
 ####################################################..........   84.2% 
Hello World
 #######################################################.......   89.5% 
Hello World
 ##########################################################....   94.7% 
Hello World
 ##############################################################   100.0% 
runTime is 0.0006635189056396484 seconds

```
