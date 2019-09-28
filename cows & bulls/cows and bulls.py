'''
    BULLS AND COWS
'''
import random


class CowsAndBullsGame:

    # Generates a number between 1000 and 9999.
    SearchedNumber = str(random.randrange(1000, 9999))

    def __init__(self):
        # The number of cows.
        self.cows_count = 0

        # The number of bulls.
        self.bulls_count = 0

        # Shows us that the game is still going.
        self.isPlaying = True

        # The number of attempts of guessing.
        self.number_of_attempts = 1

        # The maximum number of attempts the player has.
        self.max_number_of_attempts = 10

    def PlayGame(self):
        """
            Plays a turn of "Cows & Bulls" game.
            :param: None
        """

        while self.isPlaying:
            self.PlayerInput(input("{}. Enter your guess here: ".format(self.number_of_attempts)))
            self.GetBulls()
            self.GetCows()
            print("bulls = {} , cows = {}".format(self.bulls_count, self.cows_count))
            self.CheckIfMAxAttempts()
            self.CheckWin()
            self.number_of_attempts += 1

    def PlayerInput(self, player_input):
        """
            Gets the player input. Checks if his lenght is 4, otherwise the player has to enter the number again.
            :param: None
        """

        self.player_input = player_input
        while len(self.player_input) != 4:
            self.player_input = input("Enter your guess here: ")

    def GetBulls(self):
        """
            Counts how many bulls the player has in his number.
            :param: None
        """

        for pos in range(len(self.player_input)):
            if self.player_input[pos] == self.SearchedNumber[pos]:
                self.bulls_count += 1
                self.cows_count = 0

    def ScanIfCows(self, player_input_number, player_input_index):
        if player_input_number not in self.SearchedNumber:
            return True
        else:
            # pos --> position of the player input in the sought number.
            pos = self.SearchedNumber.index(player_input_number)
            # Check if resulted pos is equal with player_input_index number.
            return pos == player_input_index

    def GetCows(self):
        """
            Counts how many cows the player has in his number.
            :param: None
        """

        for index, number in enumerate(self.player_input):
            result = self.ScanIfCows(number, index)
            if not result:
                self.cows_count += 1

    def CheckWin(self):
        """
            Checks if the player_input is same as the SearchedNumber.
            :param: None
        """

        if self.player_input == self.SearchedNumber:
            print("_________________________\nCongratulations! You won!")
            print("You managed to win from {} attempts.".format(self.number_of_attempts))
            self.isPlaying = False
        elif self.player_input != self.SearchedNumber:
            self.bulls_count = 0
            self.cows_count = 0

    def CheckIfMAxAttempts(self):
        if self.number_of_attempts == self.max_number_of_attempts:
            print("You ran out of attempts! You lost the game! 🙁\nThe number was {}.".format(self.SearchedNumber))
            self.isPlaying = False

game = CowsAndBullsGame()
game.PlayGame()
