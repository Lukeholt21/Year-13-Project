from Save_Load import *

def pad_recursion(newUserID_str):
    if len(newUserID_str) == 4:
        return newUserID_str
    else:
        return pad_recursion("0"+newUserID_str)

global Users
Users=[]
def generateUserID():
    Users = loadUsers()
    
    try:
        newUserID_int = len(Users)
        newUserID_int += 1
        newUserID_str = str(newUserID_int)
        userID = pad_recursion(newUserID_str)
        print(userID)
    
        #needs to pad 0 before list_length  Use recustion   +1#
    except:
        userID = "0001"
        print(userID)
generateUserID()





    