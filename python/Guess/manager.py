from Guess.status import GuessState


class GuessManager(object):

    def __init__(self,
                 guessContents: list[any],
                 guessCount: int,
                 ) -> None:
        self.guessContents = guessContents
        self.guessCount = guessCount


    def guess(self,
              value: any,
              ) -> GuessState: pass