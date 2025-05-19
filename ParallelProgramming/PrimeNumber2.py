#multiprocessing
from multiprocessing import Process
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    prime_count = 0
    for number in range(start, end):
        if is_prime(number):
            prime_count += 1
    print(f"Process found {prime_count} primes between {start} and {end}")

if __name__ == "__main__":
    start_time = time.time()

    processes = []
    ranges = [(1, 100000), (100000, 200000), (200000, 300000), (300000, 400000)]

    for start, end in ranges:
        p = Process(target=count_primes, args=(start, end))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(f"Total time (processes): {time.time() - start_time:.2f} seconds")