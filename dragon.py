import random
import time
def displayIntro():
    print("You are in a land full of dragons. In front of you,")
    print("you see two caves. In one cave, the dragon is friendly")
    print("and will share his treasure with you. The other dragon")
    print("is greedy and hungry, and will eat you on sight.")
    good = random.randint(1,2)
    cave = ""
    while cave != 1 and cave != 2:
        cave = input("Which cave will you go into? (1 or 2)\n")
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaw and...")
    time.sleep(2)
    if cave == good:
        goodDragon()
    else:
        badDragon()
def playAgain():
    play = ""
    while play != "yes" and play != "no":
        play = raw_input("Do you want to play again? (yes or no)\n")
    if play == "yes":
        displayIntro()
    else:
        print("\n")
def badDragon():
    print("Gobbles you down in one bite!\n")
    playAgain()
def goodDragon():
    print("Gives you his treasure!\n")
    playAgain()
displayIntro()
