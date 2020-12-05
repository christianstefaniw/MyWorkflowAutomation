import os


class Execute:
    def __init__(self, opt, command):
        self.opt = opt
        self.command = command
        self.projects = "C:/Users/cpste/Desktop/Projects"
        self.intelliJ = 'C:/"Program Files"/JetBrains/"IntelliJ IDEA 2020.2"/bin/idea.bat'
        self.pycharm = 'C:/"Program Files"/JetBrains/"PyCharm 2020.2"/bin/pycharm.bat'

    @staticmethod
    def help_message():
        return '''
            -c or --connect = connect device @ 192.168.1.115
            -d = disconnect attached devices
            -o or --open + PROJECTNAME = open project in /Projects/ with IntelliJ
            --python + PROJECTNAME = open project in /Projects/ with PyCharm
            
            --cp + PROJECTNAME = add, commit, push a project, requires -m flag
                -m = commit message
                --pull = pull
                -f = force push
            '''

    def run(self):
        if self.command is None:
            print(self.help_message())
            return

        print("loading...")

        self.switch()

    def switch(self):
        if self.command == '-c' or self.command == '--connect':
            self.connect()
        elif self.command == '-d' or self.command == '--disconnect':
            self.disconnect()
        elif self.command == '-o' or self.command == '--open':
            self.open()
        elif self.command == '--python':
            self.open_python()
        elif '--cp' in self.command and '-m' in self.command:
            self.commit_and_push()
        else:
            print(self.help_message())

    # add, commit and push to GitHub
    def commit_and_push(self):

        proj_dir = self.opt[self.command.index('--cp')]
        msg = '"{}"'.format(self.opt[self.command.index('-m')])

        os.chdir(f"C:/Users/cpste/Desktop/Projects/{proj_dir}")

        if '--pull' in self.command:
            os.system("git pull")

        os.system("git add .")
        os.system(f"git commit -m {msg}")

        if '-f' in self.command:
            os.system("git push -f")
        else:
            os.system("git push")

    # open a project with IntelliJ
    def open(self):
        os.system(f"{self.intelliJ} {self.projects}/{self.opt}")

    # open a project with PyCharm
    def open_python(self):
        os.system(f"{self.pycharm} {self.projects}/{self.opt}")

    # start wireless debugging
    @staticmethod
    def connect():
        os.chdir("C:/Users/cpste/Desktop/platform-tools/")
        os.system("adb tcpip 5555")
        os.system("adb connect 192.168.1.115")

    # disconnect connected devices
    @staticmethod
    def disconnect():
        os.chdir("C:/Users/cpste/Desktop/platform-tools/")
        os.system("adb disconnect")
