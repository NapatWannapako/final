# Write a program called gusses_num_full_version.py which followong by 3 versions of guessing number game
'''
Follow this requirements:
1. Create a class called GuessnumV1
2. Create 5 private attributes: _minNum, _maxNum, _correctNum, _maxTries, _numOfGames
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
    def __init__(self, minNum=1, maxNum=10, maxTries=3):
        self._minNum = minNum
        self._maxNum = maxNum
        self._correctNum = random.randint(minNum, maxNum)
        self._maxTries = maxTries
        self._numOfGames = 0

    def playGame(self):
        self._numOfGames += 1
        while self._maxTries > 0:
            try:
                guess = int(
                    input(f'Guess a number between {self._minNum} and {self._maxNum}: '))
                if guess < self._minNum or guess > self._maxNum:
                    raise ValueError
                if guess == self._correctNum:
                    print('Congratulation! You guessed the correct number!')
                    break
                else:
                    self._maxTries -= 1
                    if guess > self._correctNum:
                        print(
                            'Your guess is too high Number of tries left:', self._maxTries)
                    else:
                        print(
                            'Your guess is too low Number of tries left:', self._maxTries)
            except ValueError:
                print('Invalid input!')

    def getNumOfGames(self):
        return self._numOfGames

    def __str__(self):
        pass


class GuessnumV2(GuessnumV1):
    def __init__(self, minNum=1, maxNum=10, maxTries=3):
        super().__init__(minNum, maxNum, maxTries)
        self._guesses = []
        self._numGuesses = 0

    def showSpecific(self):
        while True:
            try:
                guess = int(input('Enter guess number: '))
                if guess < 1 or guess > self._numGuesses:
                    raise ValueError
                print(self._guesses[guess - 1])
                break
            except ValueError:
                print('Invalid input!')

    def showGuesses(self):
        print(self._guesses)

    def playGame(self):
        super().playGame()
        self._guesses.append(self._correctNum)
        self._numGuesses += 1


class GuessnumV3(GuessnumV2):
    def guessesAvg(self):
        return sum(self._guesses) / self._numGuesses

    def guessesMax(self):
        return max(self._guesses)

    def guessesMin(self):
        return min(self._guesses)


def main():
    game = GuessnumV3()
    while True:
        choice = input('Enter your choice: ')
        if choice == 'p':
            game.playGame()
        elif choice == 's':
            game.showSpecific()
        elif choice == 'a':
            game.showGuesses()
        elif choice == 'q':
            break


if __name__ == '__main__':
    main()
