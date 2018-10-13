import random
u = "_"
#sets variable as False to see if the letter guessed exists at all in the word
letterInWord = False
#creates a list for the blanks in the words
wordList = []
#sets the wrong guesses variable
wrongGuesses = -1
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

#creates the lines for the words
if start == "yes":
    wordToGuess = (possibleWords[word])
    print(wordToGuess)
    for x in wordToGuess:
        wordList.append("_")
    print(wordList)

    while wrongGuesses < 6:
        guess = raw_input("Guess a letter. ")
        if len(guess) == 1:
            if guess:
                y = 0
                letterInWord = False
                for x in wordToGuess:
                    y += 1
                    if str(guess) == x:
                        wordList.insert(y, x)
                        wordList.remove(u)
                        letterInWord = True
                if letterInWord == False:
                    print("That letter is not in the word.")
                    wrongGuesses += 1
                    guessesLeft = 5 - wrongGuesses
                    print("You still have " + str(guessesLeft) + " guesses left.")
            print(wordList)
        else:
            print("Only guess one letter. ")
else:
    start = raw_input("Are you ready to begin? ")
