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