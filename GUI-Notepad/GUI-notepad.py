from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
	global file
	root.title("Untitled File")
	file = None
	TextArea.delete(1.0, END)
def openFile():
	global file
	file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
	if file == "":
		file = None
	else:
		root.title(os.path.basename(file))
		TextArea.delete(1.0, END)
		f = open(file, "r")
		TextArea.insert(1.0, f.read())
		f.close()

def saveFile():
	global file
	if file == None:
		file = asksaveasfilename(initialfile = "Untitled.txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
		if file =="":
			file = None
		else:
			# Save as a new file
			f = open(file, "w")
			f.write(TextArea.get(1.0, END))
			file.close()
	else:
		# Save the file
		f = open(file, "w")
		f.write(TextArea.get(1.0, END))
		file.close()
		root.title(os.path.basename(file))
def quitApp():
	root.destroy()

def cut():
	TextArea.event_generate("<<Cut>>")

def copy():
	TextArea.event_generate("<<Copy>>")

def paste():
	TextArea.event_generate("<<Paste>>")

def about():
	showinfo("Notepad", "This Notepad is developed by Priyanshu Bhattacharjee and it is OpenSource.Follow me on GitHub ID: Priyanshu-CODERX")

if __name__ == "__main__":

	#Basic Tkinter Setup

	root = Tk()
	root.title("Untitled - Notepad")
	root.wm_iconbitmap("notepad.ico")

	root.geometry("644x768")

	# Add TextArea
	TextArea = Text(root, font="lucida 13")
	file = None
	TextArea.pack(expand=True,fill=BOTH)

	# Lets create menubar

	MenuBar = Menu(root)
	# File Menu Starts
	FileMenu = Menu(MenuBar, tearoff=0)
	# To Open new file
	FileMenu.add_command(label="New", command=newFile)

	# To open existing file
	FileMenu.add_command(label="Open", command = openFile)

	#To save current file
	FileMenu.add_command(label="Save", command=saveFile)
	FileMenu.add_separator()
	FileMenu.add_command(label = "Exit", command=quitApp)
	MenuBar.add_cascade(label = "File", menu=FileMenu)
	# File menu Ends

	# Edit Menu Starts
	EditMenu = Menu(MenuBar, tearoff=0)
	#To give feature of cut, copy, paste
	EditMenu.add_command(label="Cut", command = cut)
	EditMenu.add_command(label="Copy", command = copy)
	EditMenu.add_command(label="Paste", command = paste)

	MenuBar.add_cascade(label="Edit", menu=EditMenu)
	# Edit menu ends

	# Help Menu Starts

	HelpMenu = Menu(MenuBar, tearoff=0)
	HelpMenu.add_command(label = "About Notepad", command=about)

	MenuBar.add_cascade(label="Help", menu=HelpMenu)

	# Help Menu Ends



	root.config(menu = MenuBar)

	# Adding Scrollbar
	Scroll = Scrollbar(TextArea)
	Scroll.pack(side=RIGHT, fill=X)
	Scroll.config(command=TextArea.yview)
	TextArea.config(yscrollcommand=Scroll.set)
	
	root.mainloop()