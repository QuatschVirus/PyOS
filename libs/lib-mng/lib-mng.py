import requests, sys, os, hashlib
from colorama import Fore, init

init(convert=True)


def error(error_type: str, error_line: str, error_raiser: str, error_msg: str, error_solver='', stop=False):
    print(f'''{Fore.RED}---ERROR---
An error occurred
UserInput: "{error_line}"
{error_raiser}.{error_type}: {error_msg}
Possible Solvings: {error_solver}
---ERROR---{Fore.RESET}''')
    if stop is True:
        sys.exit('ERROR')


def install(*args, command, user, alias=None):
    if user == 'root':
        for lib in args[1:]:
            lib_download = requests.get(f'https://raw.githubusercontent.com/QuatschVirus/PyOS/main/libs/{lib}/{lib}.py')
            if lib_download.status_code == 404:
                error('LibNotFound', f'DOWNLOAD libs/{lib}/{lib}.py', 'lib-mng.LibDownloader', f'A library with the name {lib} was not found.', error_solver='Refer to GitHUb for available libraries')
            else:
                with open(os.path.abspath(f'{lib}.py'), 'x') as f:
                    f.write(lib_download.content.decode())
                    print(f"Successfully downloaded {lib}")


    else:
        error("Insufficient Permissions", "LIBMNG access", "lib-mng.AccessManagment", "You dont have enough permissions to install libraries.", error_solver="Login as user root")
        return
