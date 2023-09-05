#!/usr/bin/python3

import requests
import time
import os
from pwn import *

url = input("Input the URL\n")

if not url:
    print("Incorrect URL provided. Exiting...")
else:

	count = 0

	while True:
		    
		count += 1
		response = requests.get(url)
		
		if response.status_code != 502 and response.status_code != 503:
		    warn(f"Website is finally up! {response}")
		    break   

		print(response, count)
		print("Cooldown...")
		time.sleep(60)
		os.system('clear')
