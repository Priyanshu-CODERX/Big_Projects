# GUI-Calculator

from tkinter import *
from tkinter.messagebox import showinfo



def about():
  showinfo("Calculator", "This Calculator is developed by Priyanshu Bhattacharjee and it is OpenSource.GitHub Repo: Priyanshu-CODERX/Big_Projects", )
  

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
       if scvalue.get().isdigit():
           value = int(scvalue.get())
       else:
        value = eval(screen.get())
       scvalue.set(value)
       screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("600x700")
root.title("Calculator")
root.configure(background="white")

root.wm_iconbitmap("cal.ico")
MenuBar = Menu(root)

# Help Menu Starts
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label = "About Calculator", command=about)

MenuBar.add_cascade(label="Help", menu=HelpMenu)
# Help Menu Ends


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, ipady=10, padx=10)

# Buttons 9-7
f = Frame(root, bg="white")
b = Button(f, text="9",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="8",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="7",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)
f.pack()

# Buttons 6-4
f = Frame(root, bg="white")
b = Button(f, text="6",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="5",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="4",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)
f.pack()

# Buttons 3-1
f = Frame(root, bg="white")
b = Button(f, text="3",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="2",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="1",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)
f.pack()

# Button 0, =, C
f = Frame(root, bg="white")
b = Button(f, text="=",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)

b = Button(f, text="0",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)

# Clear Button
b = Button(f, text="c",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)

f.pack()

# Arithmetic Operators Button
f = Frame(root, bg="white")
b = Button(f, text="+",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="-",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady=16)
b.bind("<Button-1>", click)
b = Button(f, text="*",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)
b = Button(f, text="/",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)
# Button "."
b = Button(f, text=".",padx=28, pady=22, font="lucida 20 bold")
b.pack(side=LEFT, padx = 12, pady = 16)
b.bind("<Button-1>", click)
f.pack()


root.config(menu = MenuBar)

root.mainloop()
