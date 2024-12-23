from Guess.status import GuessState
from random import choice


class GuessManager(object):

    def __init__(self,
                 guessContents: list[any],
                 guessCount: int,
                 ) -> None:
        self.guessContents = guessContents
        self.guessCount = guessCount
        self.target = choice(guessContents) if guessContents else None


    def guess(self,
              value: any,
              ) -> GuessState: 
        state = GuessState.WIN
        if not self.target or self.target == value: 
            return state
        elif self.target < value:
            state = GuessState.LESSER
        elif self.target > value:
            state = GuessState.GREATER

        self.guessCount -= 1
        if self.guessCount <= 0: return GuessState.LOSS
        return state
        