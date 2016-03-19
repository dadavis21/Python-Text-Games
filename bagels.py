import random
def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ""
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum
def getClues(guess, secretNum):
    if (guess == secretNum):
        return "You got it!"
    clues = []
    for i in range(0,len(guess)):
        if (guess[i] == secretNum[i]):
            clues.append("Fermi")
        elif (guess[i] in secretNum):
            clues.append("Pico")
    if (len(clues) == 0):
        return "Bagels"
    else:
        clues.sort()
        return "".join(clues)
def isOnlyDigits(num):
    if (num == ""):
        return False
    for char in num:
        if (char not in ["1","2","3","4","5","6","7","8","9"]):
            return False
    return True
def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")
NUMDIGITS = 3
MAXGUESS = 10

print("""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number. You have 10 guesses to get it.""")
while True:
    secretNum = getSecretNum(3)
    guesses = 1
    while (guesses < 11):
        guess = ""
        while (len(guess) != NUMDIGITS):
            guess = raw_input("Guess #" + str(guesses) + ":\n")
        print getClues(guess, secretNum)
        if (guess == secretNum):
            break
        guesses += 1
    if not playAgain():
        break
