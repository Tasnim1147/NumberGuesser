"""
WIN
LOSS
GREATER
LESSER
"""

from enum import Enum
from typing import Final

class GuessState(Enum):

    WIN: Final = "win"
    LOSS: Final = "loss"
    GREATER: Final = "greater"
    LESSER: Final = "lesser"

    def __str__(self):
        return self.value
    
if __name__ == "__main__":
    print(GuessState.WIN)