from Save_Load import *

global Users
Users=[]
def generateUserID():
    Users = loadUsers()

    for i in range (0,len(Users)):
        print(Users[i].firstName)

    try:
        list_length = len(data)
        #needs to pad 0 before list_length  Use recustion   +1#
    except:
        userID = "0001"
        print(userID)

###print(Users[i].userID,Users[i].firstName,Users[i].surname,Users[i].simsCode,Users[i].accessLevel,Users[i].password)

def load_example():
    Users = loadUsers()
    print(Users[0].userID)
    print(len(Users))

generateUserID()
