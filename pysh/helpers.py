from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from os import chdir
from getpass import getuser as get_username  # noqa: F401
from platform import node as network_name, python_version  # noqa: F401

def execute_code(code):
    # Capture all potential output from the code
    stdout = StringIO()
    stderr = StringIO()


    with redirect_stdout(stdout), redirect_stderr(stderr):
        return_val = exec(compile(code, '', 'exec'))

    stdout, stderr = stdout.getvalue(), stderr.getvalue()

    if return_val is None:
        # Return printed text if no return val
        if stdout:
            return stdout.rstrip()
        elif stderr:
            return stderr.rstrip()
        else:
            # Nothing was printed AND the return value is None
            return None
    else:
        return return_val


def get_cwd():
    return str(Path.cwd()).replace(str(Path.home()), "~")


def cd(new_path):
    chdir(Path(new_path).expanduser())