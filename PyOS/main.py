import sys, os, platform, time, json, yaml
from colorama import init, Fore
from psutil import virtual_memory

init(convert=True)

commands = dict()
aliases = dict()
libs = dict()
logins = dict()
logged_in = str()


def error(error_type: str, error_line: str, error_raiser: str, error_msg: str, error_solver='', stop=False):
    print(f'''{Fore.RED}---ERROR---
An error occurred
UserInput: "{error_line}"
{error_raiser}.{error_type}: {error_msg}
Possible Solvings: {error_solver}
---ERROR---{Fore.RESET}''')
    if stop is True:
        sys.exit('ERROR')


class Commands:
    @staticmethod
    def exit(*args, command, user, alias=None):
        sys.exit(f'{Fore.RED}ManualUserExit: {user}{Fore.RESET}')

    @staticmethod
    def help(*args, command, user, alias=None):
        with open(os.path.abspath('commands.json')) as g:
            helps = json.load(g)
            for command in helps.keys():
                print(f'{command} : {helps[command]}')

    @staticmethod
    def info(*args, command, user, alias=None):
        username = os.popen('whoami').read()
        if os.name == 'nt':
            username = username.split('\\')[1][:-1]
        print(f'''System Information:
| Main System: 
| | System Name: {platform.system()}
| | System Release: {platform.release()} ({platform.version()}) 
| | System Indicator: {os.name}
| | Machine Name: {platform.node()}
| | Machine Type: {platform.machine()}
| | Machine Memory: {int(virtual_memory().total / (1042 * 1042))}MB
| | Logged-in User: {username}
|
| Virtual Machine:
| | System Name: PyOS
| | System Release: {platform.python_version()[0]} ({platform.python_version()})
| | System Indicator: py
| | Machine Name: DOSTOP-{platform.node()}
| | Machine Type: {platform.machine()}
| | Machine Memory: {int(virtual_memory().total / (1042 * 1042))}MB
| | Logged-in User: {logged_in}''')

    @staticmethod
    def py(*args, command, user, alias=None):
        os.system(command)


def process_command(command: str):
    command_parsed = command.split(' ')
    if command_parsed[0] not in commands.keys() and command_parsed[0] not in aliases.keys():
        error('CommandNotFound', '§' + command, 'CommandProcessor', f'Command "{command_parsed[0]}" was not found.',
              'Use help')
    elif command in aliases.keys():
        commands[aliases[command_parsed[0]]](command_parsed, command=command, user=logged_in, alias=aliases[command_parsed[0]])
    else:
        commands[command_parsed[0]](command_parsed, command=command, user=logged_in)


def login():
    global logged_in
    valid_user = False
    valid_password = False
    user = str()
    while not valid_user:
        user = input('Username: ')
        if user.lower() == 'exit':
            sys.exit(f'{Fore.RED}LoginExit{Fore.RESET}')
        elif user not in logins.keys():
            print('This user does not exist. Enter "exit" to stop the Virtual Machine')
        else:
            valid_user = True
    while not valid_password:
        password = input('Password: ')
        if logins[user] == password:
            valid_password = True
        elif password.lower() == 'cancel':
            login()
        elif password.lower() == 'exit':
            sys.exit(f'{Fore.RED}LoginExit{Fore.RESET}')
        else:
            print('Invalid password. Enter "cancel" to select a different user, enter "exit" to stop the Virtual Machine')
    logged_in = user


os.system('title PyOS')
print('Starting PyOS Virtual Machine...')
print('Indexing built-in commands...')
built_ins = {
    'exit': Commands.exit,
    'help': Commands.help,
    'info': Commands.info,
    'py': Commands.py
}
commands.update(built_ins)
if 'dev' in sys.argv:
    print(commands.keys())
print('Collecting, loading and indexing libraries...')
with open(os.path.abspath('loadlist.txt')) as f1:
    bootload = f1.readlines()
sys.path.insert(0, os.path.abspath('libs'))
for bootloaded in bootload:
    print(f'Loading library {bootloaded}')
    try:
        lib = __import__(bootloaded)
        for command_load in lib.commands.keys():
            commands[f'{bootloaded}.{command_load}'] = lib.commands[command_load]
        libs[bootloaded] = lib
    except ModuleNotFoundError:
        error('ModuleNotFound', f'bootload {bootloaded}', 'BootLibLoader', f'The library {bootloaded} was not found', 'Move it into the subfolder libs')
    except TypeError or AttributeError:
        error('LibLoadError', f'Index commands from {bootloaded}', 'BootLibLoader', f'The commands from {bootloaded} couldn\'t be resloved correctly', 'Refer to GitHub for setting up own libraries')
print('Loading and indexing aliases for commands')
with open(os.path.abspath('aliases.yml')) as f:
    aliases = yaml.load(f, Loader=yaml.FullLoader)
print('Collecting, loading and indexing logins')
with open(os.path.abspath('users/logins.yml')) as f:
    logins = yaml.load(f, Loader=yaml.FullLoader)
print('Login to proceed:')
login()
os.system(f'cd ./users/{logged_in}/files')
if 'show' in sys.argv:
    time.sleep(5)
if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear')
print('----------PyOS----------')

while True:
    command_input = input('§')
    process_command(command_input)
