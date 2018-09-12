# Example 1: Workers output concurrently

import threading, time


def worker(name):
    for j in range(100):
        print("Worker {} - {}".format(name, j))
        time.sleep(0.5)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
