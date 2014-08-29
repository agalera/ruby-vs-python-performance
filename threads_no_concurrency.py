import threading
import sys
def func1(parte):
    i = 0
    while i<=parte:
        i+=1

total = 10000000
concurrency = int(sys.argv[1])
list_threads = []
for x in range(concurrency):
    t = threading.Thread(target=func1, args=(total/concurrency,))
    list_threads.append(t)
    t.start()
for x in list_threads:
    x.join()
