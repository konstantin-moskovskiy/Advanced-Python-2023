import concurrent.futures
import logging
import math
import os
import time

def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    chunks = [(a + i * step, a + (i + chunk_size) * step) for i in range(0, n_iter, chunk_size)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_chunk, f, a, b, chunk) for chunk in chunks]
        logging.info("Started %d tasks", len(futures))
        result = sum(future.result() for future in futures)
    return result

def integrate_chunk(f, a, b, chunk):
    acc = 0
    for i in range(int((chunk[1] - chunk[0]) / (b - a) * 100)):
        acc += f(chunk[0] + i * (b - a) / 100) * (b - a) / 100
    logging.info("Task for range %.3f - %.3f is done", chunk[0], chunk[1])
    return acc

def measure_time(f, n_jobs):
    start_time = time.monotonic()
    integrate(f, 0, math.pi / 2, n_jobs=n_jobs)
    end_time = time.monotonic()
    return end_time - start_time

cpu_num = os.cpu_count()
n_jobs_list = list(range(1, cpu_num * 2 + 1))

logging.basicConfig(filename='artifacts/medium/log.txt', level=logging.INFO)
with open('artifacts/medium/time_comparison.txt', 'w') as time_file:
    for n_jobs in n_jobs_list:
        time_taken = measure_time(math.cos, n_jobs)
        time_file.write(f"n_jobs = {n_jobs}, time taken = {time_taken:.3f} seconds\n")