def teacherClass():
    class teacher():
        def __init__(self,userID,firstName,surname,simsCode,accessLevel):
            self.userID = userID    ##PRIMARY KEY##     ##userID will be generated by the code#100-10000##
            self.firstName = firstName
            self.surname = surname
            self.simsCode = simsCode
            self.accessLevel = accessLevel 

    userID = str(input("UserID: "))
    firstName = str(input("First name: "))
    surname = str(input("Surname: "))
    simsCode = str(input("Sims code: "))
    accessLevel = 0
    userID = teacher(userID,firstName,surname,simsCode,accessLevel)
    
    #print(userID.__dict__)
#teacherClass()

def adminClass():
    class admin():
        def __init__(self,userID,firstName,surname,simsCode,accessLevel):
            self.userID = userID    ##PRIMARY KEY##     ##userID will be generated by the code#0-99##
            self.firstName = firstName
            self.surname = surname
            self.simsCode = simsCode
            self.accessLevel = accessLevel

    userID = str(input("UserID"))
    firstName = str(input("First name"))
    surname = str(input("Surname"))
    simsCode = str(input("Sims code"))
    accessLevel = 1
    userID = admin(userID,firstName,surname,simsCode,accessLevel)

def bookingClass():
    class bookings():
        def __init__(self,bookingID,authorised,userID,resourceID,lessonID):
            self.bookingID = bookingID      ##PRIMARY KEY##
            self.authorised = authorised
            self.userID =userID     ##FOREIGN KEY##
            self.resourceID = resourceID    ##FOREIGN KEY##
            self.lessonID = lessonID    ##FOREIGN KEY##

    bookingID = str(input("Booking ID : "))
    authorised = bool(input("authrised"))
    userID = str(input("UserID"))        ##Will be taken form the signed in usr##
    resourceID = str(input("resouceID"))
    lessonID = str(input("lessonID"))

    bookingID = bookings(bookingID,authorised,userID,resourceID,lessonID)

def resourceClass():
    class resource():
        def __init__(self,resourceID,location,typeEquipment,numberComputer):
            self.resourceID =resourceID
            self.location = location
            self.typeEquipment = typeEquipment
            self.numberComputer = numberComputer
    
    resourceID = str(input("ResourceID"))
    location = str(input("Location"))
    typeEquipment = str(input("typeEquipment"))
    numberComputer = str(input("numberComputer"))
    
    resourceID =resource(resoruceID,location,typeEquipment,numberComputer)

def lessonClass():
    class lesson():
        def __init__(self,lessonID,subject,classLocation,classSize,faculty,lessonTime):
            self.lessonID = lessonID    ##PRIMARY KEY##
            self.subject = subject
            self.classLocation =classLocation
            self.classSize = classSize
            self.faculty = faculty
            self.lessonTime = lessonTime

    lessonID = str(input("Lesson ID : "))
    subject = str(input("Subject : "))
    classLocation = str(input("Lesson ID : "))
    classSize = str(input("Lesson ID : "))
    faculty = str(input("Lesson ID : "))
    lessonTime = str(input("Lesson ID : "))

    lessonID = lesson(lessonID,subject,classLocation,classSize,faculty,lessonTime)