#Multiples of 3 0r 5, till 1000

Multiple_Total=0
Multiple3=0
Multiple5=0

print("This is the program #1: Print multiples of 3 and 5")
for i in range(0,1000):
    if (i%3==0 and i%5==0):
        Multiple_Total=Multiple_Total+i
    if (i%3==0):
        Multiple3=Multiple3+i 
    if (i%5==0):
        Multiple5=Multiple5+i

print ("Total of multiple of 3 and 5 below 1000 is : ", Multiple_Total)
print ("Total of multiple of 3 below 1000 is : ", Multiple3)
print ("Total of multiple of 5 below 1000 is : ", Multiple5)
print ("Total of multiple of 3 or 5 below 1000 is : ", (Multiple3+Multiple5)-Multiple_Total)
















