from Guess.status import GuessState
from random import choice


class GuessManager(object):

    def __init__(self,
                 guessContents: list[any],
                 guessCount: int,
                 ) -> None:
        self.guessContents = guessContents
        self.totalGuess = guessCount
        self.guessCount = guessCount
        self.target = choice(guessContents) if guessContents else None


    def guess(self,
              value: any,
              ) -> GuessState: 
        state = GuessState.WIN
        self.guessCount -= 1
        if not self.target or self.target == value: 
            return state
        elif self.target < value:
            state = GuessState.LESSER
        elif self.target > value:
            state = GuessState.GREATER

        if self.guessCount <= 0: return GuessState.LOSS
        return state
    
    def getGuessCount(self) -> int: return self.totalGuess - self.guessCount
        