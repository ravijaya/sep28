import threading
from time import sleep
from random import random


def worker(delay):
    """thread function"""
    t_name = threading.currentThread().name
    t_id = threading.currentThread().ident
    # sleep(delay)
    print(t_name, 'waited for the :', delay)


def main():
    """main thread"""

    list_of_threads = []

    for item in range(1, 6):
        rand_valie = random()
        t = threading.Thread(target=worker, args=[rand_valie], name=f't{item}')
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()   # block the exec main thread until the joined thread terminates

    print(threading.currentThread().name, ':prepares to terminate')



if __name__ == '__main__':
    main()