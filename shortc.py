import sys
import getopt

import Execute


def run():
    fields = 'o:tdm:f'
    longFields = ['open=', 'tcpip=', 'python=', 'cp=']

    options, args = getopt.getopt(sys.argv[1:], fields, longFields)

    option = []
    command = []

    for opt, arg in options:
        if len(opt) > 1:
            option.append(arg)
            command.append(opt)
        else:
            option = arg
            command = opt

    if len(command) == 1:
        command = command[0]

    if len(option) == 1:
        option = option[0]

    Execute.Execute(option, command).run()


if __name__ == '__main__':
    run()
