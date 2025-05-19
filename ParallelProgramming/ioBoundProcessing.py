from multiprocessing import Process
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

if __name__ == "__main__":
    start_time = time.time()

    processes = []

    for url in urls:
        p = Process(target=fetch, args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(f"Total time (processes): {time.time() - start_time:.2f} seconds")