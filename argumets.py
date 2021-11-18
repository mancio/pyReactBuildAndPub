import getopt


def argument_builder(args):
    argumentList = args

    par = {
        "path": "",
        "host": "",
        "port": "",
        "user": "",
        "pass": ""
    }

    # Options
    options = "hP:o:p:s:w:"

    # Long options
    long_options = ["help", "path =", "host =", "port =", "user =", "pass ="]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print("usage: main.py -P <path> -o <host_name> -p <port_number> -s <user_name> -w <password>")
                print("or")
                print("usage: main.py --path <path> --host <host_name> --port <port_number> --user <user_name> -pass "
                      "<password>")
                quit()

            elif currentArgument in ("-P", "--path"):
                par["path"] = currentValue
                print('path: ' + par["path"])

            elif currentArgument in ("-o", "--host"):
                par["host"] = currentValue
                print('host: ' + par["host"])

            elif currentArgument in ("-p", "--port"):
                par["port"] = int(currentValue)
                print('port: ' + currentValue)

            elif currentArgument in ("-s", "--user"):
                par["user"] = currentValue
                print('user: ' + par["user"])

            elif currentArgument in ("-w", "--pass"):
                par["pass"] = currentValue
                print('pass: ******')

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))

    return par
