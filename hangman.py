import random
HANGMANPICS = ['''

    +---+
     |   |
         |
         |
         |
         |
  =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
def getSecretWord(wordList):
    wordIndex = random.randint(0,len(wordList) - 1)
    return wordList[wordIndex]
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)] + "\n")
    print("Missed Letters: " + missedLetters + "\n")
    guess = ""
    for letter in secretWord:
        if letter in correctLetters:
            guess += letter
        else:
            guess += "_"
    print(guess + "\n")
def guessLetter(secretWord, missedLetters, correctLetters):
    guessedLetter = ""
    while True:
        guessedLetter = raw_input("Guess a letter.\n")
        guessedLetter = guessedLetter.lower()
        if guessedLetter in (missedLetters + correctLetters):
            print ("Please enter a letter that hasn't been entered")
        elif len(guessedLetter) != 1:
            print ("Please enter only one letter")
        elif not guessedLetter.isalpha():
            print("Please enter a letter in the alphabet")
        else:
            return guessedLetter
            break

missed = ""
correct = ""
secret = getSecretWord("ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split())
gameIsDone = False
print("HANGMAN")
while True:
    displayBoard(HANGMANPICS, missed, correct, secret)
    guess = guessLetter(secret, missed, correct)
    if(guess in secret):
        correct = correct + guess
        foundAllLetters = True
        for letter in secret:
            if letter not in correct:
                foundAllLetters = False
                break
        if foundAllLetters:
            gameIsDone = True
            print("Yes! The secret word is " + secret + "! You have won")
    else:
        missed = missed + guess
        if len(missed) > 5:
            print('You have run out of guesses!\nAfter ' + str(len(missed)) + ' missed guesses and ' + str(len(correct)) + ' correct guesses, the word was "' + secret + '"')
            gameIsDone = True
    if gameIsDone:
        replay = raw_input("Would you like to play again? (yes or no)\n")
        if replay == "yes":
            missed = ""
            correct = ""
            gameIsDone = False
            secret = getSecretWord("ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split())
        else:
            break
