from tkinter import *
from tkinter import  messagebox
#from Classes import *
#from tkinter import ttk

def createUser():
    def check_Create(firstName,surname,sims,password,userType):
        firstName_Pass = False
        surname_Pass = False
        sims_Pass = False
        password_Pass = False


        if firstName_Pass == False:
            if len(firstName.get()) <=20 and len(firstName.get())>0:
                firstName_Pass = True
            else:
                messagebox.showerror("First Name Error","Please enter a first name")
        
        if surname_Pass == False:
            if len(surname.get()) <= 20 and len(surname.get()) >0:
                surname_Pass = True
            else:
                messagebox.showerror("Surname Error","Please enter a surname")

        if sims_Pass == False:
            if len(sims.get()) == 3:
                sims_Pass = True
            else:
                messagebox.showerror("Sims Code Error","Please enter you 3 character sims code or initials")

        if password_Pass == False:
            if len(password.get()) <= 24 and len(password.get())>3:
                password_Pass = True
            else:
                messagebox.showerror("Password Error","Please enter a password that is between 4 and 24 characters long.")

        if firstName_Pass == True and surname_Pass == True and sims_Pass == True and password_Pass == True :
            
            def pad_recursion(newUserID_str):
                if len(newUserID_str) == 4:
                    return newUserID_str
                else:
                    return pad_recursion("0"+newUserID_str)

            global Users
            Users=[]
            def generateUserID():
                from Save_Load import loadUsers
                Users = loadUsers()
                
                try:
                    newUserID_int = len(Users)
                    newUserID_int += 1
                    newUserID_str = str(newUserID_int)
                    userID = pad_recursion(newUserID_str)
                    return userID
                    #needs to pad 0 before list_length  Use recustion   +1#
                except:
                    userID = "0001"
                    return userID
            
            userID = generateUserID()



            firstName = firstName.get()
            surname = surname.get()
            simsCode = sims.get()
            accessLevel = userType.get()
            password = password.get()

            #print(userID,firstName,surname,simsCode,accessLevel,password)
            from Save_Load import saveUser
            saveUser(userID,firstName,surname,simsCode,accessLevel,password)
            if accessLevel == 1:
                usrType = "User"
            elif accessLevel == 2:
                usrType = "Admin"
            messagebox.showinfo("New User Information",("User ID: ",userID,"Name: ",firstName,surname,"Sims Code: ",simsCode,"User Type: ",usrType))
            createUser_Form.destroy()



    createUser_Form = Toplevel(mainForm)
    createUser_Form.title("Create User")
    createUser_Form.geometry("450x200")

    firstName_lbl =Label(createUser_Form,text="First Name:")
    firstName_lbl.grid(column=0,row=0,padx=50)
    surname_lbl = Label(createUser_Form,text="Surname:")
    surname_lbl.grid(column=0,row=1,padx=100)
    sims_lbl = Label(createUser_Form,text="Sims Code:")
    sims_lbl.grid(column=0,row=2,padx=100)
    password_lbl = Label(createUser_Form,text="Password:")
    password_lbl.grid(column=0,row=3,padx=100)

    firstName = StringVar()
    firstName_ety = Entry(createUser_Form,width=15, textvariable=firstName)                                 ###firstName.get()  to get data from variable###
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


    userType = IntVar()
    user_rad = Radiobutton(createUser_Form,text="User",variable=userType,value=1)
    user_rad.grid(column=0,row=4)
    admin_rad = Radiobutton(createUser_Form,text="Admin",variable=userType,value=2)
    admin_rad.grid(column=1,row=4)

    
    create_but = Button(createUser_Form,text="Create",command=lambda:check_Create(firstName,surname,sims,password,userType))
    create_but.grid(column=0,row=5)

def loadUsers():
    global Users
    Users = []
    from Save_Load import loadUsers
    Users = loadUsers()
    
    def showuser(event):
        showuser_Form = Toplevel(loadUsers_Form)
        showuser_Form.title("Test")
        showuser_Form.geometry("400x400")

        selection = Users_lsb.curselection()            ###gets the user selected###
        cs = str(selection)
        cs_int = int(cs[1])                 ###converts tuple to string to integer###
        import Save_Load
        Users=loadUsers()

        User = Users[int(cs[1])]
        print(User.firstName)
        userID_lbl = Label(showuser_Form,text=User.firstName)
        userID_lbl.pack()



        


    loadUsers_Form = Toplevel(mainForm)
    loadUsers_Form.title("Current Users")
    loadUsers_Form.geometry("500x400")

    Users_lsb = Listbox(loadUsers_Form)
    Users_lsb.grid(column=0,row=0)

    for i in range(0,len(Users)):
        if Users[i].accessLevel == 2:
            accessLeveltemp = "Admin"
        else:
            accessLeveltemp = "User"
        Users_lsb.insert(i,(Users[i].userID,Users[i].firstName,Users[i].surname,Users[i].simsCode,accessLeveltemp))
    
    Users_lsb.bind('<Double-Button>',showuser)

    search_lbl = Label(loadUsers_Form,text="Search Database for firstname")
    search_inp = StringVar()
    search_tbx = Entry(loadUsers_Form,textvariable=search_inp)
    search_but = Button(loadUsers_Form,text="Search")

    search_lbl.grid(column=1,row=0)
    search_tbx.grid(column=1,row=1)
    search_but.grid(column=1,row=2)

    

def Login():
    global counter
    counter = 0 
    def Login_command():            
        from Save_Load import loadUsers
        Users = loadUsers()
        if len(Users) ==0:                                      ### Checks for Users in the file
            messagebox.showerror("ERROR","No users detected.")
        from Classes import userClass
        
        global counter
        
        for i in range(0,len(Users)):
            if counter > 4:             ### Checks the try limit
                messagebox.showerror("Login Error","You have exceed the current number of tries, please contact your administrator")
                break
            if userID_inp.get() == Users[i].userID:         ### Checks the inputed userID to see if it exists
                ### needs a decrypt function ###
                if password_inp.get() == Users[i].password:     ### Checks if the password is correct
                    if Users[i].accessLevel == 2:           ### Checks if is usr or admin
                        admin_Screen()
                    elif Users[i].accessLevel == 1:
                        User_Screen()
                    Login_Form.destroy()
                else:
                    messagebox.showwarning("Incorrect Information","Username or Password incorrect")
                    counter = counter + 1
            else:
                messagebox.showwarning("Incorrect Information","Username or Password incorrect")
                counter = counter + 1

    Login_Form = Toplevel(mainForm)
    Login_Form.title("Administrator Login")
    Login_Form.geometry("600x150")

    title_lbl =Label(Login_Form,text="Login")
    title_lbl.grid(column=1,row=0,padx=50)
    userID_lbl = Label(Login_Form,text="User ID")
    userID_lbl.grid(column=0,row=1,padx=100)
    password_lbl = Label(Login_Form,text="Password")
    password_lbl.grid(column=0,row=2,padx=100)

    userID_inp = StringVar()
    userID_ety = Entry(Login_Form,width=15, textvariable=userID_inp)
    userID_ety.grid(column=1,row=1,padx=10)
    password_inp = StringVar()
    password_ety = Entry(Login_Form,width=15,textvariable=password_inp)
    password_ety.grid(column=1,row=2,padx=10)

    login_but =Button(Login_Form,text="Login",command= Login_command)
    login_but.grid(column=1,row=3)
    
def admin_Screen():
    admin_Form = Toplevel(mainForm)
    admin_Form.title("Administrator")
    admin_Form.geometry("600x150")

    existingUser_but = Button(admin_Form,text="Load Users",command=loadUsers)
    existingUser_but.grid(column=0,row=0,pady=10,padx=25)
    createNewUser_but = Button(admin_Form,text="Create New User",command=createUser)
    createNewUser_but.grid(column=1,row=0,pady=10,padx=25)

def User_Screen():
    User_Form = Toplevel(mainForm)
    User_Form.title("User")
    User_Form.geometry("600x150")
    
    viewTimetable_but = Button(User_Form,text="View your timetable",command=viewTimetables)
    viewTimetable_but.grid(column=0,row=0,pady=10,padx=25)
    requestTime_but = Button(User_Form,text="Request a time from administrator",command=requestTime)
    requestTime_but.grid(column=1,row=0,pady=10,padx=25)

def viewTimetables():
    None

mainForm = Tk()
mainForm.title("Booking Login Screen")
mainForm.geometry("450x300")

welcome_lbl = Label(mainForm,text="Welcome!")
welcome_lbl.grid(column=1,row=0,pady=20,padx=25)
#teacherLogin_but = Button(mainForm,text="Teacher Login", command= teacherLogin )
#teacherLogin_but.grid(column=0,row=1,padx=50,pady=100)
Login_but =Button(mainForm,text="Login",command=Login)
Login_but.grid(column=0,row=1,padx=50,pady=100)
viewTimetables_but = Button(mainForm,text="View Time Tables",command=viewTimetables)
viewTimetables_but.grid(column=2,row=1,pady=100)
#mainForm.iconbitmap("Logo.ico")

loadUsers()

mainForm.mainloop()


