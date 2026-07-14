#threading
import threading
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
    print(f"Thread found {prime_count} primes between {start} and {end}")

start_time = time.time()

threads = []
ranges = [(1, 100000), (100000, 200000), (200000, 300000), (300000, 400000)]

for start, end in ranges:
    t = threading.Thread(target=count_primes, args=(start, end))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Total time (threads): {time.time() - start_time:.2f} seconds")