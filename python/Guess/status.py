
from enum import Enum
from typing import Final

class GuessState(Enum):

    WIN: str = "win"
    LOSS: str = "loss"
    GREATER: str = "greater"
    LESSER: str = "less"

    def __str__(self):
        return self.value
    
if __name__ == "__main__":
    print(GuessState.WIN)