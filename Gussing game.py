import random
top_of_range=input("type a number: ")
if top_of_range.isdigit(): #it checks the input is digit or not
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("please type a number larger than 0 next time:")
        quit()
else:
    print("please type a number:")
random_number=random.randint(0,top_of_range)#it gives 0 to top_of_range-1
guesses=0
while True:
    guesses=guesses+1
    user_guess=input("make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time:")
        continue
    if user_guess==random_number:
        print("you got it:")
        break
    elif user_guess>random_number:
        print("you are above the numbr!")
    else:
        print("you are below the number!")
print("you got it in",guesses,"guesses")