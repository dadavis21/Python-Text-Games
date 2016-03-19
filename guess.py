import random
name = raw_input("Hello! What is your name?\n")
myNumber = random.randint(1,20)
guess = 0
count = 0
while guess != myNumber :
    guess = input("Well, " + name +", I am thinking of a number between 1 and 20. \n Take a guess.\n")
    print(str(guess) + " " + str(myNumber))
    if guess > myNumber :
        print("Your guess is too high\n")
        count += 1
    elif guess < myNumber :
        print("Your guess is too low\n")
        count += 1
    else:
        print("Good job," + name + "! You guessed my number in " + (count + 1) + " guesses!")
