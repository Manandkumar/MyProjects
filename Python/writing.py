f =open("scores.txt","w")

while True:
        participant = input("participant name>")
        if participant =="quit":
            print("Quittinggg....")
            break
        score = inpur ("score for " + participant + ">")
        f.write(participant + "," + score +"\n")

f.close()
