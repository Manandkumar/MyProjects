# Smallest Positive Number that's divisable by 1 to 20

found = False
i = 20
while found==False:
    number = 0    # c checks if the number is the one im looking for
    for x in range(1,21):
        if i%x==0:
            number = number + 1
    if number==20: # if c = 20 then its the number im looking for
        print i
        found = True
    i = i + 1  