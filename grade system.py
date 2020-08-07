print("Enter number of Discrete math :\n")
print("Enter 1st quiz Number out of 15:\n")
a=float(input())
print("Enter 2nd quiz Number out of 15:\n")
b=float(input())
print("Enter 3rd quiz Number out of 15:\n")
c=float(input())
disquiz = (a+b+c)/3

print(disquiz)

print('Enter Number of Midterm result out of 25: \n')
dismid = float(input())
print('Enter Number of presentation result out of 8: \n')
dispre  =  float(input())
print('Enter Number of attendance result out of 7: \n')
disatt = float(input())
print('Enter Number of assignment result out of 5: \n')
disas = float(input())
print('Enter Number of final result out of 40: \n')
disfinal = float(input())
totaldis = disquiz + dismid + dispre + disatt + disas + disfinal
print(totaldis)

if totaldis > 79:
    if totaldis <= 100:
        discrete = 4

elif totaldis > 74:
    if totaldis < 80:
        discrete = 3.75

elif totaldis > 69:
    if totaldis < 75:
        discrete = 3.50

elif totaldis > 64:
    if totaldis < 70:
        discrete = 3.25

elif totaldis > 59:
    if totaldis < 65:
        discrete = 3.00

elif totaldis > 54:
    if totaldis < 60:
        discrete = 2.75

elif totaldis > 49:
    if totaldis < 55:
        discrete = 2.50
elif totaldis > 44:
    if totaldis < 50:
        discrete = 2.25
elif totaldis > 39:
    if totaldis < 45:
        discrete = 2.00

else :
    discrete = 0

print("You grade of discrete math is :",discrete)


print("Enter number of calculus math :\n")
print("Enter 1st quiz Number out of 15:\n")
a1 =  float(input())
print("Enter 2nd quiz Number out of 15:\n")
b1 = float(input())
print("Enter 3rd quiz Number out of 15:\n")
c1 = float(input())
mathquiz = (a1+b1+c1)/3

print(mathquiz)

print('Enter Number of Midterm result out of 25: \n')
mathmid  =  float(input())
print('Enter Number of presentation result out of 8: \n')
mathpre  =  float(input())
print('Enter Number of attendance result out of 7: \n')
mathatt  =  float(input())
print('Enter Number of assignment result out of 5: \n')
mathas  = float(input())
print('Enter Number of final result out of 40: \n')
mathfinal = float(input())
totalmath = mathquiz + mathmid + mathpre + mathatt + mathas + mathfinal
print(totalmath)

if totalmath>79:
    if totalmath<=100:
        math = 4

elif totalmath> 74:
    if totalmath<80:
       math = 3.75

elif totalmath> 69:
    if totalmath<75:
        math = 3.50

elif totalmath> 64:
    if totalmath<70:
        math = 3.25

elif totalmath> 59:
    if totalmath<65:
       math = 3.00

elif totalmath> 54:
    if totalmath<60:
        math = 2.75

elif totalmath> 49:
    if totalmath<55:
        math = 2.50
elif totalmath> 44:
    if totalmath<50:
        math = 2.25
elif totalmath> 39:
    if totalmath<45:
        math = 2.00

else :
    math = 0

print("You grade of discrete math is :",math)



print("Enter number of data structure :\n")
print("Enter 1st quiz Number out of 15:\n")
a2=float(input())
print("Enter 2nd quiz Number out of 15:\n")
b2=float(input())
print("Enter 3rd quiz Number out of 15:\n")
c2=float(input())
dataquiz = (a2+b2+c2)/3

print(dataquiz)

print('Enter Number of Midterm result out of 25: \n')
datamid = float(input())
print('Enter Number of presentation result out of 8: \n')
datapre = float(input())
print('Enter Number of attendance result out of 7: \n')
dataatt = float(input())
print('Enter Number of assignment result out of 5: \n')
dataas = float(input())
print('Enter Number of final result out of 40: \n')
datafinal = float(input())
totaldata = dataquiz + datamid + datapre + dataatt + dataas + datafinal
print(totaldata)

if totaldata>79:
    if totaldata<=100:
        data = 4

elif totaldata> 74:
    if totaldata<80:
        data = 3.75

elif totaldata> 69:
    if totaldata<75:
        data = 3.50

elif totaldata> 64:
    if totaldata<70:
        data = 3.25

elif totaldata> 59:
    if totaldata<65:
        data = 3.00

elif totaldata> 54:
    if totaldata<60:
        data = 2.75

elif totaldata> 49:
    if totaldata<55:
        data = 2.50
elif totaldata> 44:
    if totaldata<50:
        data = 2.25
elif totaldata> 39:
    if totaldata<45:
        data = 2.00

else :
    data = 0

print("You grade of Data structure is :",data)




print("Enter number of Electrical Circuit :\n")
print("Enter 1st quiz Number out of 15:\n")
a3=float(input())
print("Enter 2nd quiz Number out of 15:\n")
b3=float(input())
print("Enter 3rd quiz Number out of 15:\n")
c3=float(input())
cirquiz = (a3+b3+c3)/3

print(cirquiz)

print('Enter Number of Midterm result out of 25: \n')
cirmid = float(input())
print('Enter Number of presentation result out of 8: \n')
cirpre = float(input())
print('Enter Number of attendance result out of 7: \n')
ciratt = float(input())
print('Enter Number of assignment result out of 5: \n')
ciras = float(input())
print('Enter Number of final result out of 40: \n')
cirfinal = float(input())
totalcir = cirquiz + cirmid + cirpre + ciratt + ciras + cirfinal
print(totalcir)

if totalcir>79:
    if totalcir<=100:
        circuit = 4

elif totalcir> 74:
    if totalcir<80:
        circuit = 3.75

elif totalcir> 69:
    if totalcir<75:
        circuit = 3.50

elif totalcir> 64:
    if totalcir<70:
        circuit = 3.25

elif totalcir> 59:
    if totalcir<65:
        circuit = 3.00

elif totalcir> 54:
    if totalcir<60:
        circuit = 2.75

elif totalcir> 49:
    if totalcir<55:
        circuit = 2.50
elif totalcir> 44:
    if totalcir<50:
        circuit = 2.25
elif totalcir> 39:
    if totalcir<45:
        circuit = 2.00

else :
    circuit = 0

print("You grade of Electrical circuit is :",circuit)


print("Enter the Number of Elelctrical circuit lab: ")
labc = float(input())

if labc>79:
    if labc<=100:
        circuitlab = 4

elif labc> 74:
    if labc<80:
        circuitlab = 3.75

elif labc> 69:
    if labc<75:
        circuitlab = 3.50

elif labc> 64:
    if labc<70:
        circuitlab = 3.25

elif labc> 59:
    if labc<65:
        circuitlab = 3.00

elif labc> 54:
    if labc<60:
        circuitlab = 2.75

elif labc> 49:
    if labc<55:
        circuitlab = 2.50
elif labc> 44:
    if labc<50:
        circuitlab = 2.25
elif labc> 39:
    if labc<45:
        circuitlab = 2.00

else :
    circuitlab = 0

print("Enter the Number of Data structure lab: ")
labd = float(input())


if labd >79:
    if labd <=100:
        datalab = 4

elif labd > 74:
    if labd <80:
        datalab = 3.75

elif labd > 69:
    if labd <75:
        datalab = 3.50

elif labd > 64:
    if labd <70:
        datalab = 3.25

elif labd > 59:
    if labd <65:
        datalab = 3.00

elif labd > 54:
    if labd <60:
        datalab = 2.75

elif labd > 49:
    if labd <55:
        datalab = 2.50
elif labd > 44:
    if labd <50:
        datalab = 2.25
elif labd > 39:
    if labd <45:
        datalab = 2.00

else :
    datalab= 0



totalresult =( datalab + (data*3) + (discrete*3) + circuitlab + (circuit*3) + (math*3) ) / 14

print("You grade of discrete math is :",discrete)
print("You grade of ordinary & partial differential equation is :",math)
print("You grade of Data structure is :",data)
print("You grade of data structure lab is :",datalab)
print("You grade of electrical circuit is :",circuit)
print("You grade of electrical circuit lab is :",circuitlab)
print("Your result in the semester is SGPA: ",totalresult)