'''
    HANGMAN --- GAME
'''

from RandomWords import RandomWordGenerator as generator


class PlayHangmanGame:
    # The given word to guess.
    HANGING_GIVEN_WORD = generator()

    # The maximum of chances you have.
    HANGING_CHANCE_MAX_NUM = 6

    # Player name.
    HANGING_PLAYER_NAME = input("Enter your name: ")

    # List with the sliced given word.
    HANGING_GIVEN_WORD_LIST = [char for char in HANGING_GIVEN_WORD]

    def __init__(self):
        # Condition so the game keeps going if is no win.
        self.isPlaying = True

        # The chance count you begin with.
        self.chanceCount = 0

        # Displays "_" as much as the word has.
        self.showHiddenWord = ["_ " for char in self.HANGING_GIVEN_WORD]

		# Displays the showHiddenWord after name request.
        tmpShowHiddenWord = [self.HANGING_GIVEN_WORD_LIST[0], ] + self.showHiddenWord[1:]
        for char in tmpShowHiddenWord:
            print(char, end=' ')
        print('\n')
		
    def PlayTheGame(self):
        """
            Play a turn of Hangman game.
            param: none
            :return none:
        """
        while self.isPlaying:

            # Gets input from player, letter or whole word.
            player_input = input("Enter a letter/whole word here: ")
            self.player_input = player_input

            # Gives a hint
            self.showHiddenWord[ 0 ] = self.HANGING_GIVEN_WORD_LIST[ 0 ]

            self.ReplaceWhitespaces()
            self.ChancesCounter()
            self.CheckIfGameOverByChances()
            self.CheckWinIfWholeWord()
            self.CheckWinLetterByLetter()

    def ReplaceWhitespaces(self):
        """
            If it's a whitespace in the given word, replace "_" in showHiddenWord with whitespace.
            param: none
        """
        for index, val in enumerate(self.HANGING_GIVEN_WORD_LIST):
            if " " == val:
                self.showHiddenWord[ index ] = " "

    def CheckWinIfWholeWord(self):
        """
            If you introduce the whole correct word, you win.
            param: none
            :return none:
        """
        if self.player_input == self.HANGING_GIVEN_WORD:
            self.showHiddenWord = self.player_input
            self.isPlaying = False
            print("{} won.\n________________\nCongratulations!".format(self.HANGING_PLAYER_NAME))
            return

    def ChancesCounter(self):
        """
            HANGING_LEFT_CHANCES --> counts how many chances you remained with.
            param: none
        """
        if (self.player_input not in self.HANGING_GIVEN_WORD_LIST):
            if (self.player_input.upper() not in self.HANGING_GIVEN_WORD_LIST):
                if (self.player_input != self.HANGING_GIVEN_WORD):
                    self.chanceCount += 1
                    HANGING_LEFT_CHANCES = self.HANGING_CHANCE_MAX_NUM - self.chanceCount
                    print("You have {} chances left.You lost {} chance/s already.".format(HANGING_LEFT_CHANCES,
                                                                                          self.chanceCount))

    def CheckIfGameOverByChances(self):
        """
            If you ran out of chances, is game over.
            param: none
        """
        self.HangmanGraphicDisplay()

        if self.chanceCount == self.HANGING_CHANCE_MAX_NUM:
            self.isPlaying = False
            print("{} ran out of chances.\nGame over...\nThe word was {}".format(self.HANGING_PLAYER_NAME,
                                                                                 self.HANGING_GIVEN_WORD.upper()))

    def CheckWinLetterByLetter(self):
        """
            If the word is introduced letter by letter, verifies if it's a win.
            param: none
            :return none:
        """
        if self.showHiddenWord == self.HANGING_GIVEN_WORD_LIST:
            self.isPlaying = False
            print("{} won.\n________________\nCongratulations!".format(self.HANGING_PLAYER_NAME))
            return

    def HangmanGraphicDisplay(self):
        """
            Displays the hanged man if you guess incorrectly a letter.
            param: None
        """
        if self.chanceCount == 0:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|__________   ")

        elif self.chanceCount == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|__________   ")

        elif self.chanceCount == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|__________   ")

        elif self.chanceCount == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|__________   ")

        elif self.chanceCount == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|__________   ")

        elif self.chanceCount == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|__________   ")

        elif self.chanceCount == 6:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|__________   ")

        self.TakeLowerOrUpperLetters()

    def TakeLowerOrUpperLetters(self):
        """
            Takes your input both as lower case and upper case.
            param: none
        """
        for i in range(len(self.HANGING_GIVEN_WORD_LIST)):
            if self.player_input == self.HANGING_GIVEN_WORD_LIST[i]:
                self.showHiddenWord[i] = self.player_input
            elif self.player_input.upper() == self.HANGING_GIVEN_WORD_LIST[i]:
                self.showHiddenWord[i] = self.player_input.upper()
            print(self.showHiddenWord[i], end=' ')
        print('\n')


Play = PlayHangmanGame()
Play.PlayTheGame()
