# Python script ask the user to enter his name with restrictions of special characters and numbers:
def checkName():
    check = True
    user_name = input('Enter your Name: ')
    if user_name == "":
        print("Please enter your name.")
        check = False
        exit(102)
    else:
        for character in user_name:
            if character in '0123456789':
                print("Numbers are not allowed in names")
                check = False
                exit()
            elif character in '!@#$%^&*()_+=~}{:"?><,.':
                print ("Special character are not allowed in names ")
                check = False
                exit()
            elif character in "'":
                print("Special character are not allowed in names ")
                check = False
                exit()
    if check == True:
        print("Your name is registered")

checkName()