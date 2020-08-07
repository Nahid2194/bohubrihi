password_bank = {'Nahid':8421,'Jahid':1234,'Joni':2345}
match = False
x =0


while x<5:
    print("Enter Your Name: ")
    name = input()
    if name in password_bank:
        for i in range(0,3):
            print("Enter Your Password ")
            password = input()
            if int(password) in password_bank.values():
                match = True
                print("Access Granted!!")
                break
            else:
                print("Your Password is Wrong Enter again "+'You have '+str(2-i)+' tries left')
    else:
        print("There is no such name in the password_bank try again")
    x= x+1
    if match:
        break

