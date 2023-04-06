import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_fibonacci_sync(n, results):
    start_time = time.time()
    for i in range(10):
        fibonacci(n)
    end_time = time.time()
    results.append(('sync', end_time - start_time))

def run_fibonacci_threads(n, results):
    start_time = time.time()
    threads = []
    for i in range(10):
        t = threading.Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    results.append(('threads', end_time - start_time))

def run_fibonacci_processes(n, results):
    start_time = time.time()
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end_time = time.time()
    results.append(('processes', end_time - start_time))

if __name__ == '__main__':
    n = 20
    results = []
    run_fibonacci_sync(n, results)
    run_fibonacci_threads(n, results)
    run_fibonacci_processes(n, results)
    with open('artifacts/results.txt', 'w') as f:
        for method, time in results:
            f.write(f'{method}, num of repeats: {n}, time: {time}\n')