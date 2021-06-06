# PyOS

A lightweight kind of operating system that can be run in nothing more than a simple console window. It alone only has basic functions, but that's the point: You can customize it almost fully. You can write libraries or programs that can be run/used with it. They need a specific formatting, refer to the Guide on "How to write a Library/Program". Any help and ideas are welcome, just make a pull request. If you upload your own versions of this, please credit me. It's not needed per license, but I would very much appreciate it.

It's not tested very much, so I can not assure it's running properly on every environment. You can report your testing results

## Warning
This is NOT a standalone operating system or a virtual machine. It's just a funny little thing I programmed during an internet outage. It's not secure at all, and should not be used for important things.

## Installation
If you want to install this, follow these guidelines. Choose what's best for you, and use to your will:

### 1. Decide, which variant you want to install
This comes in different variants for you to download. You can find them in the folder "Downloads". You're best to go with choosing one of the folowing variants:

#### Lite
The lite variant only includes the basic runtime (the folder "PyOS" as given). If you just want to, for example, get an example of command processing, I will recommend you this variants

#### Recommended
This variant includes the folder "PyOS" with some libraries installed, for example [...]. Suggested for normal users.

#### Full
This variant includes ALL libraries and programs uploaded in this repository.

#### Installer
This is a special one. It doesn't include anything from the above directly, just a couple of shell scripts, which download and install the variant they are named after, for example `PyOS-1.2.6-Full.sh` would be the linux Installation script for the "Full" variant of the version `1.2.6`. These variants will be uploaded as the bin files for the corresponding release

### 2. Install all requirements
This system needs some additional libraries, `pyyaml` and `colorama`. If not already installed, do it by downloading the "requirements.txt" file and running the command `pip install -r requirements.txt` in the same directory

### 3. Install the system
Install the variant you selected. You can do one of the following:

#### Install via the executable files
You can install it with the shell files provided as the bin files in a release or out of the `downloads/installer` folder.
Currently, only a Windows Executable Installer (exe) is available, but more options will eventually be added soon.

