# -*- coding: utf-8 -*-
"""
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).
Sample Output
The output of a winning game should look like this...

	Loading word list from file...
	55900 words loaded.
	Welcome to the game Hangman!
	I am thinking of a word that is 4 letters long.
	-------------
	You have 8 guesses left.
	Available letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Good guess: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! You've already guessed that letter: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: s
	Oops! That letter is not in my word: _ a_ _
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqrtuvwxyz
	Please guess a letter: t
	Good guess: ta_ t
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqruvwxyz
	Please guess a letter: r
	Oops! That letter is not in my word: ta_ t
	------------
	You have 6 guesses left.
	Available letters: bcdefghijklmnopquvwxyz
	Please guess a letter: m
	Oops! That letter is not in my word: ta_ t
	------------
	You have 5 guesses left.
	Available letters: bcdefghijklnopquvwxyz
	Please guess a letter: c
	Good guess: tact
	------------
	Congratulations, you won!
          
And the output of a losing game should look like this...

	Loading word list from file...
	55900 words loaded.
	Welcome to the game Hangman!
	I am thinking of a word that is 4 letters long.
	-----------
	You have 8 guesses left.
	Available Letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 7 guesses left.
	Available Letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: b
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 6 guesses left.
	Available Letters: cdefghijklmnopqrstuvwxyz
	Please guess a letter: c
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 5 guesses left.
	Available Letters: defghijklmnopqrstuvwxyz
	Please guess a letter: d
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 4 guesses left.
	Available Letters: efghijklmnopqrstuvwxyz
	Please guess a letter: e
	Good guess: e_ _ e
	-----------
	You have 4 guesses left.
	Available Letters: fghijklmnopqrstuvwxyz
	Please guess a letter: f
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 3 guesses left.
	Available Letters: ghijklmnopqrstuvwxyz
	Please guess a letter: g
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 2 guesses left.
	Available Letters: hijklmnopqrstuvwxyz
	Please guess a letter: h
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 1 guesses left.
	Available Letters: ijklmnopqrstuvwxyz
	Please guess a letter: i
	Oops! That letter is not in my word: e_ _ e
	-----------
	Sorry, you ran out of guesses. The word was else. 
          

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.

Why does my Output Have None at Various Places?

None is a keyword and it comes from the fact that you are printing the result of a function that does not return anything. For example:

    def foo(x):
        print(x)
              
If you just call the function with foo(3), you will see output:
    3   #-- because the function printed the variable
            
However, if you do print(foo(3)), you will see output:
    3     #-- because the function printed the variable
    None  #-- because you printed the function (and hence the return)
              
All functions return something. If a function you write does not return anything (and just prints something to the console), then the default action in Python is to return None
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Welcome to the game, Hangman!")
    print ("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = ''
    guessesLeft = 8
    print ("------------")
    while True:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print ("------------")
        if guessesLeft <= 0:
            print ("Sorry, You've ran out of guesses. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations! You've won!")
            break
