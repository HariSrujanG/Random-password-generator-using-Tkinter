from tkinter import*
import random

def generate():    
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%&*"
    mix = upper+lower+numbers+symbols
    a = l.get()
    L = int(a)
    pw = "".join(random.sample(mix,L))
    p.set(pw)

pwd = Tk()
pwd.title('Password generator')
pwd.geometry('300x300')
pwd.configure(bg='cyan')

l = StringVar()
p = StringVar()

#head
lbl = Label(pwd, text="Password Generator", font=("Timesnew roman",16), bg="skyblue")
lbl.grid(row=1,column=1, pady=10, padx=10,)

#length
lbl = Label(pwd, text="Enter the length of the password", font=("Timesnew roman",12), bg="cyan")
lbl.grid(row=3, column=1, pady=10 , padx=10)
txt = Entry(pwd, textvariable=l, width=5,font=("Unispace", 12),) 
txt.grid(row=4, column=1, pady=10, padx=10)

#generate button
btn = Button(pwd, text="Generate", bg="grey", fg="skyblue", command=generate )
btn.grid(row=6, column=1, pady=10, padx=10)

#passwd
lbl = Label(pwd, text="Password", font=("Timesnew roman",12), bg="cyan")
lbl.grid(row=10,column=1, pady=10, padx=10)
txt = Entry(pwd, textvariable=p, width=25, font=("Unispace", 12) )
txt.grid(row=11, column=1, pady=10, padx=10)

pwd.mainloop()
