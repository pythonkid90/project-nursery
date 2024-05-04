# Pysh & Shpy - Interactive Python Shells

## Pysh

Pysh is an interactive Python console that includes shell commands too, so you can `ls` and `cd` to your heart's content while still being able to use Python features.

Here are some features of Pysh:

*   Execute Python code directly in the terminal.
*   Get information about your environment like username, Python version, and network name.
*   Navigate directories using the \`cd\` command.
*   Exit the shell using \`exit\` or \`quit\`.

Shpy
----

Shpy is a shell-first variant of Pysh that prioritizes shell command execution. It attempts to run commands using your system shell first, falling back to Python execution if the shell command fails.

Shpy is ideal for users who frequently work with both shell commands and Python code within the same interactive session.

Shpy inherits all the features of Pysh, with the added behavior of prioritizing shell execution.

## Installation

To use pysh (or shpy), you'll need Python installed on your computer.

Then, you can clone this repository onto your device.

    ```bash
    git clone https://github.com/pythonkid90/pysh
    ```

Next, run pysh.

    ```bash
    python3 pysh/pysh/pysh.py
    ```

For shpy, do

    ```bash
    python3 pysh/pysh/shpy.py
    ```
