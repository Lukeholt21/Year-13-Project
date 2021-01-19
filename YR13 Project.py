from tkinter import *
#from tkinter import ttk

def createUser():
    
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

    createUser_Form = Toplevel(mainform)
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
    user_rad.grid(column=0,row=0)
    admin_rad = Radiobutton(createUser_Form,text="Admin")
    admin_rad.grid(column=1,row=1)

    create_but = Button(createUser_Form,text="Create",command=None)

def teacherLogin():
    teacherlogin_Form = Toplevel(mainForm)
    teacherlogin_Form.title("Teacher Login")
    teacherlogin_Form.geometry("600x150")

    title_lbl = Label(teacherlogin_Form,text="Login")
    title_lbl.grid(column=1,row=0,padx=50)
    userID_lbl = Label(teacherlogin_Form,text="User ID")
    userID_lbl.grid(column=0,row=1,padx=100)
    password_lbl = Label(teacherlogin_Form,text="Password")
    password_lbl.grid(column=0,row=2,padx=100)
    
    userID = StringVar()
    userID_ety = Entry(teacherlogin_Form,width=15, textvariable=userID)
    userID_ety.grid(column=1,row=1,padx=10)
    password = StringVar()
    password_ety = Entry(teacherlogin_Form,width=15,textvariable=password)
    password_ety.grid(column=1,row=2,padx=10)

def adminLogin():
    def Login_command():

        counter = 0
        Valid = False
        while counter < 4:
            for userID in users:
                None

    adminLogin_Form = Toplevel(mainForm)
    adminLogin_Form.title("Administrator Login")
    adminLogin_Form.geometry("600x150")

    title_lbl =Label(adminLogin_Form,text="Login")
    title_lbl.grid(column=1,row=0,padx=50)
    userID_lbl = Label(adminLogin_Form,text="User ID")
    userID_lbl.grid(column=0,row=1,padx=100)
    password_lbl = Label(adminLogin_Form,text="Password")
    password_lbl.grid(column=0,row=2,padx=100)

    userID = StringVar()
    userID_ety = Entry(adminLogin_Form,width=15, textvariable=userID)
    userID_ety.grid(column=1,row=1,padx=10)
    password = StringVar()
    password_ety = Entry(adminLogin_Form,width=15,textvariable=password)
    password_ety.grid(column=1,row=2,padx=10)

    login_but =Button(adminLogin_Form,text="Login",command= Login_command)
    login_but.grid(column=1,row=3)

def viewTimetables():
    None

mainForm = Tk()
mainForm.title("Booking Login Screen")
mainForm.geometry("600x300")

welcome_lbl = Label(mainForm,text="Welcome!")
welcome_lbl.grid(column=1,row=0,pady=20)
teacherLogin_but = Button(mainForm,text="Teacher Login", command= teacherLogin )
teacherLogin_but.grid(column=0,row=1,padx=50,pady=100)
adminLogin_but =Button(mainForm,text="Admin Login",command=adminLogin)
adminLogin_but.grid(column=1,row=1,padx=50,pady=100)
viewTimetables_but = Button(mainForm,text="View Time Tables",command=viewTimetables)
viewTimetables_but.grid(column=2,row=1,padx=50,pady=100)
mainForm.iconbitmap("Logo.ico")

mainForm.mainloop()
