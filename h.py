import requests
import concurrent.futures

url = "https://vgmlinks.fun/thcmvj000"

def check_url(i):
    current_url = url + str(i)
    response = requests.get(current_url)
    if response.status_code == 200:
        print("Exist:", current_url)
        return current_url
    else:
        return None

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(check_url, i) for i in range(1, 1000000000000)]

    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            break

print("Done!")
