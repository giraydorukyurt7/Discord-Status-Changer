print("File has been succesfully created")

import tkinter as tk

class TheGui:

	def __init__(self):
		self.root = tk.Tk()
	## Title
		self.root.title("helloworld.py")
	## Window Size")
		self.root.geometry("500x10")
	## Start The Loop
		self.root.mainloop()
TheGui()