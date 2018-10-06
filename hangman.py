import random
#sets the wrong guesses variable
wrongGuesses = 0
#list of possible words to guess
possibleWords = ["salem", "nymph", "boston", "stocks", "pentagram", "occult", "devil", "witchcraft", "rituals"]
#picks a random number for list
word = random.randint(0,8)
#sets variable name and asks for the name of the user
name = raw_input("What is your name? ")
#sets the story
print("Hi, " + str(name) + ". " + "My name is Robert, and I'm the man that might be hanged. Your job is to correctly guess the word to save my life.")
print("I am a man from the 1600s being wrongfully accused of witchcraft.")
print("I am counting on you, " + str(name) + " to set me free.")
print("There are six villainous people out there determined to slander my good name.")
print("Thereby providing you with six rare opportunities to defend me.")
print("For each person you fail to defend me from, I lose a chance at life.")
start = raw_input("Are you ready to begin? ")

letter = "w"
print type(letter)

if start == "yes":
    wordToGuess = (possibleWords[word])
    print(wordToGuess)
    print "\n"
    for x in wordToGuess:
        print "_" ,

    print "\n"
    while wrongGuesses < 6:
        guess = input("Guess a letter. ")
        print type(guess)

        #if type(guess) == int:
        #    print("This here is an integer.")
        #else:
        #    print("This is not an integer.")

        print guess
        if type(guess) == str:
            print type(guess)
            if len(guess) == 1:
                for x in wordToGuess:
                    if str(guess) == x:
                        print("correct")
        else:
            print("Only guess one letter. ")
else:
    start = raw_input("Are you ready to begin? ")
