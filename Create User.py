from tkinter import *

firstName_Pass = False
surname_Pass = False
sims_Pass = False
password_Pass = False

firstName = "Luke"
surname = "Holt"
sims = "lho"
password ="root"

while firstName_Pass == False:
    if len(firstName) <=20 and len(firstName)>0:
        firstName_Pass = True
    else:
        print("Please enter first name.")

while surname_Pass == False:
    if len(surname) <= 20 and len(surname) >0:
        surname_Pass = True
    else:
        print("Please enter surname.")

while sims_Pass == False:
    if len(sims) == 3:
        sims_Pass = True
    else:
        print("Please enter your sims code.")

while password_Pass == False:
    if len(password) <= 24 and len(password)>3:
        password_Pass = True
    else:
        print("Please enter a password that is between 4 and 24 characters long.")

createUser_Form = Tk()
createUser_Form.title("Create User")
createUser_Form.geometry("400x600")

firstName_lbl =Label(createUser_Form,text="First Name")
firstName_lbl.grid(column=0,row=0,padx=50)
surname_lbl = Label(createUser_Form,text="Surname")
surname_lbl.grid(column=0,row=1,padx=100)
sims_lbl = Label(createUser_Form,text="Sims Code")
sims_lbl.grid(column=0,row=2,padx=100)
password_lbl = Label(createUser_Form,text="Password")
password_lbl.grid(column=0,row=3,padx=100)

firstName = StringVar()
firstName_ety = Entry(createUser_Form,width=15, textvariable=firstName)
firstName_ety.grid(column=1,row=0,padx=10)
surname = StringVar()
surname_ety = Entry(createUser_Form,width=15, textvariable=surname)
surname_ety.grid(column=1,row=1,padx=10)
sims = StringVar()
sims_ety = Entry(createUser_Form,width=15, textvariable=sims)
sims_ety.grid(column=1,row=2,padx=10)
password = StringVar()
password_ety = Entry(createUser_Form,width=15,textvariable=password)
password_ety.grid(column=1,row=3,padx=10)

user_rad = Radiobutton(createUser_Form,text="User")
user_rad.grid(column=0,row=4)
admin_rad = Radiobutton(createUser_Form,text="Admin")
admin_rad.grid(column=1,row=4)

create_but = Button(createUser_Form,text="Create",command=None)

createUser_Form.mainloop()