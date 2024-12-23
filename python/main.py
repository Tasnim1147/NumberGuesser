from typing import Optional
from enum import Enum
from Guess.manager import *
from Guess.status import GuessState as gs
from Guess.number import *
from Guess.difficulty import GuessDifficulty as gd
from cmd import Cmd

class cliState(Enum):

    INIT = "choice "
    GAME = "guess "

    def __str__(self):
        return self.value

class GuessCLI(Cmd):

    
    def __init__(self, 
                 completekey = "tab", 
                 stdin = None, 
                 stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.prompt: str = "Enter your choice: "
        self.diffs = [gd.EASY, gd.MEDIUM, gd.HARD]
        self.state = cliState.INIT
        self.difficulty: GuessDifficulty = None
        self.manager: GuessNumber = None
        print("Welcome to the Number Guessing Game!.\nI'm thinking of a number between 1 and 100.\n")

    def preloop(self):
        self.promptDifficulty()
        return super().preloop()    
    
    def precmd(self, 
               line: str
               ) -> str:
        line = str(self.state) + line
        return super().precmd(line)
    
    def promptDifficulty(self):
        print("Please select the difficulty level:")
        for idx, diff in enumerate(self.diffs):
            print(f"{idx + 1}. {diff} ({diff(100)}) choices")

    def do_exit(self, 
                arg: str
                ) -> bool:
        return True
    
    def do_guess(self,
                 arg: str
                 ) -> Optional[bool]:
        try:
            guess = int(arg)
            res = self.manager.guess(guess)
            if res == gs.WIN:
                print(f"Congratulations! You guessed the correct number in {self.manager.getGuessCount()} attempts.")
                return True
            elif res == gs.LOSS:
                print(f"Alas! No more attempt left.")
                return True
            else:
                print(f"Incorrect! The number is {res} than {guess}.")

        except:
            print(f"Invalid guess: {arg}")

    def do_choice(self,
                  arg: str
                  ) -> Optional[bool]:
        if arg:
            try:
                choice = int(arg)
                if (1 <= choice <= 3):
                    self.difficulty = self.diffs[choice - 1]
                else: raise IndexError()
                print(f"\nGreat! You have selected the {self.difficulty} difficulty level.")
                print("Let's start the game!\n")
                self.manager = GuessNumber.fromRange(lo=1, 
                                                    hi=101, 
                                                    difficulty=self.difficulty)
                self.prompt = "Enter your guess: "
                self.state = cliState.GAME
            except IndexError:
                print(f"Choice out of bound: {arg}")
                self.preloop()
            except ValueError:
                print(f"Choice is not a number: {arg}")
                self.preloop()


def main(): 
    guessCli = GuessCLI()
    guessCli.cmdloop()

if __name__ == "__main__": main()