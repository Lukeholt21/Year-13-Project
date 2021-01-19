from tkinter import *

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
        None

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