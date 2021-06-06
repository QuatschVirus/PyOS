# lib-mng (Library Manager)
This is a library for installing and managing libraries from the repository

## Commands
NOTE: As for all libraries, every command in a library needs to be called with `[library name].[command]`

### install
Install libraries by name, seperated with spaces. This one is only able to install the latest releases, since it doesn't load them from their seperate repositories.

### uninstall
Delete libraries by name, seperated with spaces. It also deletes an entry on the loadlist if it's on there. I recommend a restart of the system for it to all work

### update
Update libraries by name, seperated with spaces. It installs the newest versions from GitHub. Use --all to update all installed libraries. Again, I recommend a restart of the system to use the changes

### list
#### list available
List all libraries you could install. It lists it with the name you can use for installation.

#### list installed
List all installed libraries.

### loadlist
#### loadlist add
Add libraries to the loadlist. The libraries on the loadlist are loaded on system boot.

#### loadlist remove
Remove libraries from the loadlist