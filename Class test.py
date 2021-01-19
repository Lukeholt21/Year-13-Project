class teacher():
    def __init__(self,userID,firstName,surname,simsCode):
        self.userID = userID
        self.firstName = firstName
        self.surname = surname
        self.simsCode = simsCode

userID = str(input("UserID"))
firstName = str(input("First name"))
surname = str(input("Surname"))
simsCode = str(input("Sims code"))
userID = teacher(userID,firstName,surname,simsCode)

print(userID.__dict__)