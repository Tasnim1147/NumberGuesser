from Guess.manager import GuessManager
from Guess.difficulty import GuessDifficulty
from Guess.status import GuessState

class GuessNumber(object):
    def __init__(self,
                 contents: list[int],
                 difficulty: GuessDifficulty = GuessDifficulty.EASY,
                 ) -> None:
        self.manager = GuessManager(guessContents=contents,
                                    guessCount=difficulty(len(contents)))
        
    @classmethod
    def fromRange(cls,
                  lo: int,
                  hi: int,
                  step: int = 1,
                  difficulty: GuessDifficulty = GuessDifficulty.EASY,
                  ) -> "GuessNumber":
        contents = list(range(lo, hi, step))
        return cls(contents, difficulty)
    
    @classmethod
    def fromList(cls,
                 contents: list[int],
                 difficulty: GuessDifficulty = GuessDifficulty.EASY,
                 ) -> "GuessNumber":
        return cls(contents, difficulty)
    
    def guess(self,
              value: int
              ) -> GuessState:
        return self.manager.guess(value=value)
    
    def getGuessCount(self) -> int: return self.manager.getGuessCount()