#Fibonacci Series
from typing import Counter


Num1=0
Num2=1
Temp =0
sum=0
while Temp<=4000000:
    Temp=Num1+Num2
    if(Temp%2==0):
        sum=sum+Temp
    Num1=Num2
    Num2=Temp
   
print("Sum of all the Even  Fibonaaci Number under 4 Million is: ",sum)
