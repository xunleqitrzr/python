from tkinter import *
import tkinter as tk
import subprocess
import os

root = tk.Tk()
root.title("Website Code Getter v2.4")
root.geometry("400x200")
root.resizable(False, False)

labelURL = tk.Label(root, font=("times", 15, "bold"), text="URL + /file.fileEnding [not required]").grid(row=1, column=1)
entryURL = tk.Entry(root)
entryURL.place(x=50,y=28, width=250, height=25)

def submit_url():
	global url
	url = entryURL.get()
	writeOut = subprocess.run(['curl', url], stdout=subprocess.PIPE).stdout.decode('utf-8')

	file = open("output.txt", "w")
	file.write(writeOut)
	file.close()

submitURL = tk.Button(root, text="Submit", command=submit_url).grid(row=3, column=3)

root.mainloop()