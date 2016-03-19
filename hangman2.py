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
  =========''','''
    +----+
    |    |
   [O    |
   /|\   |
   / \   |
         |
  ==========''', '''
    +----+
    |    |
   [O]   |
   /|\   |
   / \   |
         |
  ==========''']

words = {'color':'red orange yellow green blue indigo violet white black brown'.split(),
 'shape':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
 'fruit':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
 'animal':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}
def getSecretWord(wordDictionary):
    secretKey = random.choice(list(wordDictionary.keys()))
    secretWord = random.choice(wordDictionary[secretKey])
    return secretWord
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

missed, correct, secret, gameIsDone = ["","", getSecretWord(words), False]
print("HANGMAN")
while True:
    for key in list(words.keys()):
        if secret in words[key]:
            if key == "animal": print("You are guessing an " + key)
            else: print("You are guessing a " + key)
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
        if len(missed) > 7:
            print('You have run out of guesses!\nAfter ' + str(len(missed)) + ' missed guesses and ' + str(len(correct)) + ' correct guesses, the word was "' + secret + '"')
            gameIsDone = True
    if gameIsDone:
        replay = raw_input("Would you like to play again? (yes or no)\n")
        if replay == "yes":
            missed, correct, secret, gameIsDone = ["","", getSecretWord(words), False]
        else:
            break
