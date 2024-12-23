from enum import Enum
from typing import Final
from math import log2, ceil, floor

class GuessDifficulty(Enum):

    EASY: Final = lambda size: ceil(size/2)
    HARD: Final =  lambda size: floor(log2(size)) if size > 1 else size
    MEDIUM: Final = lambda size: min((GuessDifficulty.EASY(size) + 
                                      GuessDifficulty.HARD(size)) // 2, size)

    def __str__(self):
        return self.value
    
    def __call__(self,
                 size: int
                 ) -> int:
        if (self == GuessDifficulty.EASY or
            self == GuessDifficulty.MEDIUM or
            self == GuessDifficulty.HARD):
            return self.value(size)
        else:
            raise ValueError(f"Invalid difficulty type: {self}")
        

if __name__ == "__main__":
    feasy = GuessDifficulty.EASY
    fmed = GuessDifficulty.MEDIUM
    fhard = GuessDifficulty.HARD

    for size in range(100):
        a = feasy(size)
        b = fmed(size)
        c = fhard(size)
        assert(a >= b >= c)
            