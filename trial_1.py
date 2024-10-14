from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("PROJECT")

cv = Canvas(root, bg="blue", height="500", width="500")
cv.place(x=0, y=0)

l1 = Label(cv, text="W E L C O M E ", height=2, bg="orange", fg="white", font="verdana 10 bold underline ")
l1.place(x=200, y=20)

l2 = Label(cv, text="WELCOME TO JEEVITH FIRST PROJECT", bg="blue", fg="white", font="helvetica 12 bold underline")
l2.place(x=10, y=60)

l3 = Label(cv, text="Enter Username : ", bg="blue", fg="white", font="helvetica 10")
l3.place(x=10, y=90)

l4 = Label(cv, text="Enter password : ", bg="blue", fg="white", font="helvetica 10")
l4.place(x=10, y=120)

l5 = Label(cv, text="Enter phone no. :", bg="blue", fg="white", font="helvetica 10")
l5.place(x=10, y=150)

e1 = Entry(cv)
e1.place(x=125, y=90)

e2 = Entry(cv,show="*")
e2.place(x=125, y=120)

e3 = Entry(cv)
e3.place(x=125, y=150)

def click():
    s1 = e2.get()
    if s1.strip() != "Jeevith#2005":
        response = messagebox.askquestion("Question", "Wrong password. Do you want to continue?")
        if response == 'no':
            exit(0)

Button(cv, text="Submit", command=click).place(x=125, y=180)

root.mainloop()