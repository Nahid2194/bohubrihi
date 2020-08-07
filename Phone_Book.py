Phone_book = {'Nahid': 1910125428,'Jahid': 1990081563,'Joni': 984635}
x =0
while x<5:
    print("Enter Your Name(Press Enter to Exits): ")
    name = input()
    if name == '':
        break
    if name in Phone_book:
        print('The Contact Number of '+name+' is '+str(Phone_book[name]))
    else:
        print("There is no such PhoneBook.Do you want add it??")
        desc = input()
        if desc == 'yes':
            print("Enter the number")
            num = input()
            Phone_book[name]=num
            print('Dictionary Updated')
        elif desc == 'no':
            print("Do you want to quit??")
            desc = input()
            if desc == 'yes':
                break
            else:
                print("Keep searching")
    x = x+1

