from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession, print_formatted_text as print, HTML
from prompt_toolkit.lexers import PygmentsLexer

from pygments.lexers.python import PythonLexer
from pygments.lexers.shell import BashLexer

from subprocess import run
from traceback import format_exc
from os import environ

from helpers import network_name, python_version, get_username, get_cwd, cd, execute_code


class PyshLexer(PythonLexer, BashLexer):
    pass



style = Style([
    ('', 'ansiblack'),
    ('device', 'ansipurple'),
    ('path', 'ansicyan underline'),
    ('arrow', 'ansiblue'),
])

message = [
    ('class:device', get_username()),
    ('', '@'),
    ('class:device', network_name()),
    ('', ' '),
    ('class:path', get_cwd()),
    ('class:arrow', ' > '),
]
default_message = list(message)

session = PromptSession(message, style=style, lexer=PygmentsLexer(PyshLexer))

print(HTML(
    f"Welcome to <ansiyellow>pysh</ansiyellow>, the python shell. \n"
    f"<ansiblue>Running Pysh <b>0.1.0</b>.</ansiblue> "
    f"<ansired>Shell path: <b>{environ['SHELL']}</b>.</ansired> "
    f"<ansiyellow>Python version: <b>{python_version()}</b>.</ansiyellow>"
))
command = session.prompt()

while True:
        if command.endswith(":") or command.endswith("\\"):
            extra_line_message = ("." * (len(''.join([message_seg[1] for message_seg in message])) - 3))
            command = session.prompt(extra_line_message)
        elif message[-1][1] == ("...") and command is None:
            command = session.prompt(default_message)
        else:
            command = session.prompt()

        # Hardcoded command patches
        if command.startswith("cd"):
            new_path = command.split("cd")[1]

            if not new_path:
                new_path = "~"

            cd(new_path)

            message[4] = ('class:path', get_cwd())
        if command.strip() == "exit" or command.strip() == "quit":
            break

        try:
            print(execute_code(command))
        except Exception:
            exception = format_exc()

            try:
                run(command, shell=True, executable=environ["SHELL"])
            except Exception:
                print(exception)
                continue
