'''
Follow this requirements:
1. Create a class called GuessnumV1
2. Create 5 private attributes: __minNum, __maxNum, __correctNum, __maxTries, __numOfGames
3. Create 3 constructor: default constructor, constructor with 2 parameters, constructor with 3 parameters
4. Create 2 methods: playGame(), getNumOfGames(), getMinNum(), getMaxNum(), getMaxTries(), getCorrectNum()
5. Method playGame() will let user guess the number and return the number of tries
6. Create a subclass called GuessnumV2
7. Create 2 private attributes: guesses which is list of integer, numGuesses
8. Create 3 constructor: super() to call the constructor of GuessnumV1, constructor with 3 parameters
9. Create 3 methods: showSpecific(), showGuesses(), playGames()
10. Method showSpecific() will show the specific guess after user type 'g'
11. Method showGuesses() will show all guesses after user type 'a'
12. Method playGames() This method will call method playGame(), showSpecific(), and showGuess() and keep running until the user types 'q'
13. Create a subclass called GuessnumV3 
14. Create 3 methods: guessesAvg(), guessesMax(), guessesMin()
15. Method guessesAvg() will return the average of guesses
16. Method guessesMax() will return the maximum of guesses
17. Method guessesMin() will return the minimum of guesses
18. Create a main function to test the program

'''
import random


class GuessnumV1:
    pass


class GuessnumV2(GuessnumV1):
    pass


class GuessnumV3(GuessnumV2):
    pass


if __name__ == '__main__':
    pass
