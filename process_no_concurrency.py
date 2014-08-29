from multiprocessing import Process
import sys
def func1(parte):
    i = 0
    while i<=parte:
        i+=1

total = 10000000
concurrency = int(sys.argv[1])
list_process = []
for x in range(concurrency):
    t = Process(target=func1, args=(total/concurrency,))
    list_process.append(t)
    t.start()
for x in list_process:
    x.join()
