#! python3
import tkinter as tk
from tkinter import messagebox
import subprocess, sys
try:
	subprocess.call([r"Test.bat"])

	HEIGHT = 600
	WIDTH = 800

	root = tk.Tk()

	root.resizable(False, False)
	root.winfo_toplevel().title("Lets spam some emails!")
	
	can = tk.Canvas(root, height=HEIGHT, width=WIDTH)
	can.pack()

	frameSpam = tk.Frame(root, bg='black')
	frameSpamBackground = tk.Frame(frameSpam, bg='red')
	frameLogin = tk.Frame(root)

	frameSpam.place(relx=.05, rely=.1, relheight=.8, relwidth=.8)
	frameSpamBackground.place(relx=.02, rely=.02, relheight=.95, relwidth=.95)
	frameLogin.place(relx=.85, rely=0, relheight=1, relwidth=.15)
	title = tk.Label(root, text="Simple Email Spam App", cursor='fleur') 
	title.place(anchor='n', relx=.5)

	sessionLogin = {}
	sessionMessage = {}
	numOfMessages = 1;

	def convert():
		numOfMessages = numOfMessagesEntry.get();
		print(numOfMessages)

	# Spam methods	
	def insertSessionMessage():
	    sessionMessage["sendTo"] = sendToEmail.get()
	    sessionLogin["message"] = sendMessage.get("1.0", 'end-1c')
	    convert()
	    printSpam()

	# Login methods
	def insertLoginInfo():
	    sessionLogin["user"] = entLoginUser.get()
	    sessionLogin["pass"] = entLoginPass.get()

	def showSessionLogin():
	    sessionLogin.setdefault("user", "no one currently logged in")
	    sessionLogin.setdefault("pass", "no one currently logged in")
	    tk.messagebox.showinfo("Logged in", "User: " + sessionLogin.get("user") + "\nPass: " + sessionLogin.get("pass"))

	# Pepe elements
	pepePath = 'tenor.gif'
	background_pepe = tk.PhotoImage(file=pepePath)
	backLabel = tk.Label(root, image=background_pepe)
	backLabel.place(anchor='se', relx=1, rely=1)

	# All login elements
	labelForLoginUser = tk.Label(frameLogin, text="Enter email username: ")
	entLoginUser = tk.Entry(frameLogin)
	labelForLoginPass = tk.Label(frameLogin, text="Enter email password: ")
	entLoginPass = tk.Entry(frameLogin, show='*')
	butUser = tk.Button(frameLogin, text='Login', command = insertLoginInfo)
	butCheckLoggedIn = tk.Button(frameLogin, text='who is logged in?', command = showSessionLogin, activebackground='blue', activeforeground='white')

	# All login elements packed
	labelForLoginUser.pack()
	entLoginUser.pack()
	labelForLoginPass.pack()
	entLoginPass.pack()
	butUser.pack()
	butCheckLoggedIn.pack()


	def printSpam():
		for i in range(10069):
			f = open('we are number 1 ' + str(i) + '.txt', 'w+')
		tk.messagebox.showinfo("Spam Successful!", "sent, " + numOfMessagesEntry.get() + " messages saying " + sendMessage.get("1.0", 'end-1c') + " to: " + sendToEmail.get())

	# All spam elements
	emailLabel = tk.Label(frameSpam, text='Who u gunna spam?', bg='red', fg='white')
	sendToEmail = tk.Entry(frameSpam, justify='center', width='47')
	messageLabel = tk.Label(frameSpam, text="What the message?", bg='red', fg='white')
	sendMessage = tk.Text(frameSpam, width='35', height='15')
	numOfLabel = tk.Label(frameSpam, text='How many timez?', bg='red', fg='white')
	numOfMessagesEntry = tk.Entry(frameSpam, width='2')
	sendToBut = tk.Button(frameSpam, text='send', command = insertSessionMessage)

	# All spam elements placed
	emailLabel.place(relx=.1, rely=.15)
	sendToEmail.place(anchor='n', relx=.5, rely=.15)
	messageLabel.place(relx=.1, rely=.2)
	sendMessage.place(anchor='n', relx=.5, rely=.2)
	numOfLabel.place(relx=.32, rely=.75)
	numOfMessagesEntry.place(anchor='n', relx=.5, rely=.75)
	sendToBut.place(anchor='n', relx=.5, rely=.8)
	
	root.mainloop()
except:
	tk.messagebox.showinfo("What", "this is the big of errors man")
	sys.exit()

