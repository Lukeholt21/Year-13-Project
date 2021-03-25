from Save_Load import *

global Users
Users=[]
def generateUserID():
    #try:
    Users = loadUsers()
    print(Users[0].userID)
    print(len(Users))

    Users

    for i in range (0,len(Users)):
        print(Users[i].firstName)
    #except:
    #    User = "0001"
    #    print(User)

generateUserID()
