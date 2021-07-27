import json
import time
import os , sys
import requests
import os , requests , urllib3 , time
from colorama import Fore
from random import uniform
StartReq= None
Welcome_Text =""" -----------------------------------------
||                ZeNmAxE              ||
||                                     ||
||               Sms Bomber            ||
----------------------------------------- """
proxy = {'https': '127.0.0.1:8000'}
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"

def Welcome():
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX+Welcome_Text)
    time.sleep(0.25)
    print(Fore.GREEN + "[1]  " + Fore.LIGHTCYAN_EX + "Start SmS Bomber")
    print(Fore.GREEN + "[2]  " + Fore.LIGHTCYAN_EX + "About Me")
    print(Fore.GREEN + "[3]  " + Fore.LIGHTCYAN_EX + "Exit")
    Ask_Request()


def TestInternet():
    page = None
    URL = "https://api.myip.com"
    try:
        print("Checking Your Internet ...")
        page = requests.get(URL, timeout=3)
        page.raise_for_status()
        p1 = "Your Internet Connection Is Ok ...\n"
        for x in p1:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(uniform(0, 0.4))
        time.sleep(2)
        TestPing()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
def TestPing():
    URL = "https://api.myip.com"
    page = requests.get(URL)
    ip_json = json.loads(page.text)['ip']
    country_json = json.loads(page.text)['country']
    print("Your Country Is " + Fore.LIGHTRED_EX + country_json + Fore.WHITE +
    "\nAnd Your Ip is " + Fore.LIGHTRED_EX + ip_json + Fore.WHITE , flush=True)
    if "Iran" in country_json:
        print("Turn On Your"+Fore.LIGHTGREEN_EX + " VPN " + Fore.WHITE +
            "Than Start " + Fore.LIGHTMAGENTA_EX + "WiliBomber" + Fore.WHITE)
        time.sleep(1)
        quit()
    elif "Iran" not in country_json:
        print("Welcome To SmS Bomber , Your Connection is " +Fore.LIGHTYELLOW_EX+"Secure"+Fore.WHITE)
        time.sleep(7)
        Welcome()

def Ask_Request():
    ask = input("Selct Your Request: ")
    if ask == "1"  :
        StartReq = 1
        print(StartReq)
        print("hh")
    elif ask == "2" :
        print("hello")
        time.sleep(1) 
        Ask_Request()   
    elif ask == "3" :
        quit()
    else:
        print("Wrong Request Code ...")
        time.sleep(1) 
        Ask_Request()
def Phonenumberdata():
    global Pask, SMSNumber
    Pask = input("Enter Your Phone Number Without +98:")
    Check_Pask = input("Your Phone Number is +98"+Pask +" ? (Y / N)")
    if Check_Pask == "Y":
        SMSNumber = input("How Many SMS You Want Send?: ")
        
    elif Check_Pask == "N":
        Phonenumberdata()
    else:
        print("Enter Again")
        

TestInternet()


