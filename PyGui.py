#! python3
import tkinter as tk
from tkinter import messagebox
import subprocess
subprocess.call([r"PyGui.bat"])

HEIGHT = 600
WIDTH = 800

root = tk.Tk()

root.resizable(False, False)

can = tk.Canvas(root, height=HEIGHT, width=WIDTH)
can.pack()

frame = tk.Frame(root, bg='red')
frame2 = tk.Frame(root, bg='blue')
frame.place(relx=.25, rely=.25, relheight=.5, relwidth=.5)
frame2.place(relx=.6, rely=.1, relheight=.1, relwidth=.1)

a = []

def addToA(e):
    a.append(e)
    
def showBox():
    for i in range(len(a)):
        messagebox.showinfo("title", a[i])

def insert():
    a.append(inputField.get())
    

but = tk.Button(frame2, text='dothings', command = showBox)
but.pack()
but2 = tk.Button(frame, text='enter', command = insert)

inputField = tk.Entry(frame)

inputField.pack()

but2.pack()

root.mainloop()

