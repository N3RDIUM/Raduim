from _typebase import *

class Terminal(Terminal):
    def __init__(self):
        self._text = '''
        Radium Terminal v0.1
        Created and maintained by the 1up Community.
        '''
        super().__init__(self._text)

    def callback(self, _input):
        if _input == "help":
            self._print("This is the first command of the radium terminal!")
