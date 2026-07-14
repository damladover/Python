# io_bound_thread.py
import threading
import requests
import time

urls = [
    "https://example.com",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2"
]

def fetch(url):
    response = requests.get(url)
    print(f"{url} - Status Code: {response.status_code}")

start_time = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=fetch, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Total time (threads): {time.time() - start_time:.2f} seconds")