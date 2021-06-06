# Libraries
Here you can find the newest versions of all working libraries that were submitted via pull request or directly created by a contributer. Refer to their documentation for detailed info on how to use these.

## What is a library?
Libraries implement new commands into the system to work with.

## I want to create my own library. How do i do that?
Libraries have some standardized formats and names for some objects. There is a `template.py` in here to get a view of it.

First, the library script is loaded using `import`. This means, it is run on loading, and the loading process can only continue when your script has finished. So, don't include long loops.

All available commands should be put in a dictionary called `commands` which is formatted as following: The key is the name of the command that gets called by the user, the value of it is the function as a variable that you want to run when the command is called.

All commands should take exactly these arguments in this configuration: `*args, command, user, alias=None`.

### *args
the arguments the command consists of. This is basically the user input, splitted in it's contents. This includes the actual command called.

### command
This is just the command string that the user ran.

### user
The user that ran this command

### alias
This is only not None, when an alias for this command is called. It contains the command that was actually run internally as a full string.
