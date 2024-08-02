import random
import time
score = 0
def mathsquestions():
    global score
    n = random.randint(1, 10)
    ni = random.randint(1,10)
    nig = n * ni
    question1 = int(input(f"""
What Is {n} x {ni}?
*******************************
Type You're Answer Here(Type 699 For You're Score): """))
    if question1 == nig:
        print("Good, Right Answer!")
        score += 1
        mathsquestions()
    elif(question1 == 699):
        print(f"You're Score is", {score})
        mathsquestions()
    else:
        print("Nuh-uh Try Again!")
        print(f"BTW You're Score Is: {score}")
        score = 0
        mathsquestions()
def startprogram():
    agreement = input("Are You Ready? (Type \"yes\" To Countinue)")
    if agreement == "yes":  
        time.sleep(1)
        print("Good")
        mathsquestions()
    else:
        print("You Have To Type yes Bro")
        time.sleep(1)
        startprogram()
startprogram()