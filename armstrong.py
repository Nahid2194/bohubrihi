N= int(input())
temp=N
sum=0

while N != 0:
    rem = N%10
    N = N//10
    sum = sum+ (rem**3)
if sum == temp:
    print("the Number is armstrong")
else:
    print("Not Armstrong")