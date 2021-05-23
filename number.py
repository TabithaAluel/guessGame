import random
number=random.randrange(1,60)
guess=int(input("I want you to guess a number between 1,60: "))
while guess !=number:
    if guess < number:
        print("Ooops! you need to guess higher. Give it a try one more time")
        guess=int(input("\nI want you to guess a number between 1,60: "))
    else:
            print("Ooops! you need to guess lower. Give it a try one more time")
            guess=int(input("\nI want you to guess a number between 1,60: "))
print("Congrats! You guess the number correctly")            


