import time
import requests


def RTT(url):
    
    time1 = time.time()

    req = requests.get(url)

    time2 = time.time()

    rtt_time = round(time2 - time1, 3)

    print(f'The Round-Trip Time is: {rtt_time} Seconds ')


url = 'http://www.google.com'
RTT(url)
