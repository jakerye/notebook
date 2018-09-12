# Example 1: Workers output sequentially

import threading, time


def worker(name, lock):
    for j in range(5):
        lock.acquire()
        print("Worker {} - {}".format(name, j))
        time.sleep(0.5)
        lock.release()


if __name__ == "__main__":
    threads = []
    lock = threading.RLock()
    for i in range(5):
        t = threading.Thread(target=worker, args=(i, lock))
        t.daemon = True
        threads.append(t)
        t.start()

    while True:
        time.sleep(1)
