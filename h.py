import requests
import concurrent.futures
import os

url = "https://vgmlinks.fun/thcmvj000"
file_name = "output.txt"

def check_url(i):
    current_url = url + str(i)
    response = requests.get(current_url)
    if response.status_code == 200:
        with open(file_name, "a") as file:
            file.write(current_url + "\n")  # Add a newline character
        print("Exist:", current_url)
        return current_url
    else:
        return None

if os.path.exists(file_name):
    os.remove(file_name)

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    futures = [executor.submit(check_url, i) for i in range(1, 1000000000000)]

    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            break

print("Done!")
