# Number Guessing Game

import random

start = int(input("Where you start: "))
end = int(input("Where you end: "))
randomise = random.randint(start,end)
user_in = int(input("Guess Number: "))
attempt = 1

while start <= user_in <= end:
    if user_in == randomise:
        print(f"Matched, Attempt = {attempt}")
        break
    elif user_in < randomise:
        print(f"Too Low, Attempt = {attempt}")
        user_in = int(input("Guess Number: "))
    else:
        print(f"Too High, Attempt = {attempt}")
        user_in = int(input("Guess Number: "))
    attempt += 1
else:
    print(f"Oops! You guess wrong. Attempt = {attempt}")
    user_in = int(input("Guess Number: "))