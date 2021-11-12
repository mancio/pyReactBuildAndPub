## Py React build

### An app to build your react web app and upload by ftp

### How to use

usage: main.py -P <path> -o <host_name> -p <port_number> -s <user_name> -w <password>

or

usage: main.py --path <path> --host <host_name> --port <port_number> --user <user_name> -pass <user_password>

path = full path example: C:\\blabla\\foo\\project_folder

example:

main.py -P C:\\Users\\mancio\\IdeaProjects\\MancioTechWeb -o mysite.com -p 21 -s web@mysite.com -w Gigi989Paoli97

### What the app does:

1. execute npm run build
2. delete static folder on remote server
3. upload content of build folder on remote server