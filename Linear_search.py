Mark = [78,98,56,87,35]

Search_Mark = int(input("Enter search a Subject mark: "))
p = 0
for i in range(len(Mark)):
    if Mark[i] == Search_Mark:
       p= 1
       break
    else:
       p = 0
if p==1:
     print("Yes Find This Mark")
else:
     print("Didn't Find The Mark")