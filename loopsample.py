import progress
Time = progress.timer()

for i in range(0,20,1):
    print("Hello World")
    progress.bar(i,19)

Time.end()
