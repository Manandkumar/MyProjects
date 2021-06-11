#Largest palindrome product

for i in range(100,999):
    for j in range (100,999):
        usern = i*j   
        temp = usern
        reverse = 0
        while (usern>0):
            dig=usern%10
            reverse=reverse*10+dig
            usern=usern//10
        if(temp==reverse):
            print("The number is a Palindrome",reverse)

