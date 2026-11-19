# Number Guessing Game 

import random

start_number = int(input("Where you start: "))
end_number = int(input("Where you end: "))
number = random.randint(start_number,end_number)
user_input = int(input("Guess Number: "))

attempt = 1

while start_number <= user_input <= end_number:
    if number == user_input:
        print(f"Number matched on {number}, Attempt = {attempt}")
        break
    elif number > user_input:
        print(f"Mismatched. Too Low. Attempt = {attempt}")
        user_input = int(input("Guess Number: "))
    elif number < user_input:
        print(f"Mismatched. Too High. Attempt = {attempt}")
        user_input = int(input("Guess Number: "))
    attempt += 1
else:
    print(f"Oops! Out of range. Attempt = {attempt}")    