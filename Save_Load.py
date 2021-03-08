import pickle

def saveUser():
    fh = open("User_Data.p","wb")         ##The entry should be encrypted##
    pickle.dump(teacher,fh)
    fh.close()

def bookingSave():
    fh = open("Bookings.p","wb")
    pickle.dump(booking,fh)
    fh.close()

def lessonSave():
    fh = open("Lessons.p","wb")
    pickle.dump(lesson,fh)
    fh.close()

def resourceSave():
    fh = open("Resources.p","wb")
    pickle.dump(resource,fh)
    fh.close()


def loadUsers():
    fh = open("User_Data.p","rb")
    users_Loaded = pickle.load(fh)
    fh.close()

def loadBookings():
    fh = open("Booking.p","rb")
    bookings_Loaded = pickle.load(fh)
    fh.close()

def loadLessons():
    fh = open("Lessons.p","rb")
    lessons_Loaded = pickle.load(fh)
    fh.close()

def loadResources():
    fh = open("Resources.p","fh")
    resources_Loaded = pickle.load(fh)
    fh.close()


