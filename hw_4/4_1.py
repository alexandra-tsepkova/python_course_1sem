import time
from threading import Thread
from multiprocessing import Process


def fib(n=100000):
    a_0 = 0
    a_1 = 1
    for _ in range(n):
        a_0, a_1 = a_1, a_0 + a_1
    return a_0


def run_multiple_threads(n=10):
    thread_list = [Thread(target=fib) for _ in range(n)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    return


def run_multiple_processes(n=10):
    process_list = [Process(target=fib) for _ in range(n)]
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()
    return


# Measure time with threads
time_start_t = time.time()
run_multiple_threads()
time_end_t = time.time()
duration_t = time_end_t - time_start_t
print("Threads:", duration_t)

# Measure time with processes
time_start_p = time.time()
run_multiple_processes()
time_end_p = time.time()
duration_p = time_end_p - time_start_p
print("Processes:", duration_p)


