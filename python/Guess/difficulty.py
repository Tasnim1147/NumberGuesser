from enum import Enum
from math import log2, ceil, floor

class GuessDifficulty(Enum):

    EASY: str = "easy"
    MEDIUM: str = "medium"
    HARD: str = "hard"

    def __str__(self):
        return self.value
    
    def __call__(self,
                 size: int
                 ) -> int:
        if (self == GuessDifficulty.EASY): return ceil(size/ 2)
        elif (self == GuessDifficulty.HARD): return floor(log2(size)) if size > 1 else size
        elif (self == GuessDifficulty.MEDIUM):
            return (self.EASY(size) + self.HARD(size)) // 2
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

    print(GuessDifficulty["EASY"])
            