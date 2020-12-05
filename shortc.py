import sys
import getopt

from shortcuts.execute import Execute


def run():
    fields = 'o:cdm:f'
    long_fields = ['open=', 'connect', 'python=', 'cp=']

    options, args = getopt.getopt(sys.argv[1:], fields, long_fields)

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

    Execute(option, command).run()


if __name__ == '__main__':
    run()
