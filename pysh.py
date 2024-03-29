from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession, print_formatted_text as print
from prompt_toolkit.lexers import PygmentsLexer

from pygments.lexers.python import PythonLexer
from pygments.lexers.shell import BashLexer

from subprocess import run
from platform import node, python_version
from traceback import format_exc
from os import environ, chdir
from getpass import getuser
from pathlib import Path

class PyshLexer(PythonLexer, BashLexer):
    pass


def get_cwd():
    return str(Path(".").resolve()).replace(str(Path.home()), "~")


style = Style([
    ('', 'ansiblack'),
    ('device', 'ansiblue'),
    ('path', 'ansicyan underline'),
    ('arrow', 'ansibrown ansiyellow'),
])

message = [
    ('class:device', getuser()),
    ('', '@'),
    ('class:device', node()),
    ('', ' '),
    ('class:path', get_cwd()),
    ('class:arrow', ' > '),
]

session = PromptSession(message, style=style, lexer=PygmentsLexer(PyshLexer))


print(f"Welcome to pysh, the python shell. \n"
      f"Running Python {python_version()} and shell is located at {environ['SHELL']}")

while True:
    try:
        command = session.prompt()
        if command.startswith("cd"):
            new_path = command.split("cd")[1]
            if not new_path:
                new_path = "~"

            chdir(Path(new_path).expanduser())

            message[4] = ('class:path', get_cwd())

        print(eval(command))

    except Exception:
        exception = format_exc()

        try:
            run(command, shell=True, executable=environ['SHELL'])
        except Exception:
            print(exception)
