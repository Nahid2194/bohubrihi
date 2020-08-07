n=int(input("Enter a Number: "))
sp= " "
st="*"

for i in range(1,n+1,1):
   print(sp*(n-i)+(st*(i*2-1)))
