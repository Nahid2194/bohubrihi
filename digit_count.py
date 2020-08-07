digit = int(input())
count = 0
while digit != 0:
    digit = digit // 10
    count= count+1
print(count)