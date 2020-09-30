"""thread sync using semaphore"""

import threading
from time import sleep
from random import random
import logging

logging.basicConfig(format='%(threadName)s : %(message)s')


def worker(delay, lock):
    """thread function"""
    t_name = threading.currentThread().name
    t_id = threading.currentThread().ident
    # sleep(delay)
    logging.warning('awaits for the lock')

    with lock:
        """critical section"""
        logging.warning('acquired the lock')
        print(t_name, 'waited for the :', delay)
        sleep(1)
        logging.warning('releases the lock')


def main():
    """main thread"""
    lock = threading.Semaphore(1)
    list_of_threads = []

    for item in range(1, 6):
        rand_value = random()
        t = threading.Thread(target=worker, args=[rand_value, lock])
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()  # block the exec main thread until the joined thread terminates

    print(threading.currentThread().name, ':prepares to terminate')


if __name__ == '__main__':
    main()
