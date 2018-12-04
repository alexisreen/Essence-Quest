import codecs
import lockfile
from lockfile import LockFile
class UserAccount():
	info = []
	username = ""
	password = ""
	username_encoded = ""
	password_encoded = ""
	player_name = ""
	level = 0

	def CheckCredentials(username, password):
		lock = LockFile("Account.txt")
		lock.break_lock()
		fp = open("Account.txt", "r")
		if fp == FileNotFoundError:
			return -1
		cred_list = []
		cred_list = fp.readlines()
		if username+' ' == cred_list[i][i]:
			if password+' ' == cred_list[i][i]:
				break
				return 0
			else:
				return 1
		else:
			return 2

	def AccountCreation():
		username = str(input("Enter Username: "))
		password = str(input("Enter Password: "))
		username_encoded = codecs.encode(username, 'rot_13')
		password_encoded = codecs.encode(password, 'rot_13')
		player_name = str(input("Enter Player Name: "))
		info = [username, password, username_encoded, password_encoded, player_name]
		fp = open("Account.txt", "a+")
		i = 0
		if fp != FileNotFoundError:
			while(i < 5):
				fp.write(info[i]+' ')
				i += 1
			fp.write('\n')
			fp.close()
			lock = LockFile("Account.txt")
			lock.acquire()
			with lock:
				print("Success!")
			return 0
		else:
			return 1

	def Loggin():
		usr = str(input("Enter Username: "))
		pwd = str(input("Enter Password: "))
		if UserAccount.CheckCredentials(usr, pwd) == 0:
			print("Success!")
			return 0
		elif UserAccount.CheckCredentials(usr, pwd) == 1:
			print("Wrong Password")
			return 1
		elif UserAccount.CheckCredentials(usr, pwd) == 2:
			print("Wrong Username")
			return 2
		else:
			print("Wrong Loggin Credentials!")
			return -1