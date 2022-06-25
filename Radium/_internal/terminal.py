from _typebase import *
import os
from pathlib import Path

class Terminal(Terminal):
    def __init__(self):
        self._text = '''
        Radium Terminal v0.1
        Created and maintained by the 1up Community.
        '''
        super().__init__(self._text)
        self.setInput(">")

        # Cd to user's home directory (windows CMD)
        print(Path.home())
        os.chdir(Path.home())
        print("Changed directory to " + os.path.abspath(os.curdir))
        self._terminaldetails = {
            "current_directory": os.path.abspath(os.curdir),
        }

    def callback(self, _input):
        _input = _input.replace("> ", "")
        if _input == "help":
            self._print("This is the first command of the radium terminal!")
        elif "cd" in _input.lower():
            try:
                os.chdir(_input.split("cd ")[1])
                self._terminaldetails["current_directory"] = os.path.abspath(os.curdir)
                self._print("Changed directory to " + self._terminaldetails["current_directory"])
            except Exception as e:
                self._print(f"<div style=\"color:red\">Failed to change directory because of error: {e}</div>")
        elif _input.lower() in ["cd", "ls"]:
            # get output from os.system("dir")
            output = os.popen("dir").read()
            self._print(output)
        else:
            self._print("<div style=\"color:red\">This command doen't exist!</div>")
