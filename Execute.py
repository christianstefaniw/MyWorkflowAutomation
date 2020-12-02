import os


class Execute:
    def __init__(self, opt, command):
        self.opt = opt
        self.command = command
        self.projects = "C:/Users/cpste/Desktop/Projects"
        self.intelliJ = 'C:/"Program Files"/JetBrains/"IntelliJ IDEA 2020.2"/bin/idea.bat'
        self.pycharm = 'C:/"Program Files"/JetBrains/"PyCharm 2020.2"/bin/pycharm.bat'

    @staticmethod
    def helpMessage():
        return '''
            -t = connect device @ 192.168.1.115
            -d = disconnect attached devices
            -o or --open + PROJECTNAME = open project in /Projects/ with IntelliJ
            --python + PROJECTNAME = open project in /Projects/ with PyCharm
            '''

    def run(self):
        if self.command is None:
            print(self.helpMessage())

            return

        print("loading...")

        self.switch()

    def switch(self):
        if self.command == '-t' or self.command == '--tcpip':
            self.tcpip()
        elif self.command == '-d':
            self.disconnect()
        elif self.command == '-o' or self.command == '--open':
            self.open()
        elif self.command == '--python':
            self.openPython()
        elif '--cp' in self.command and '-m' in self.command:
            self.commitAndPush()
        else:
            print(self.helpMessage())

    # add, commit and push to GitHub
    def commitAndPush(self):

        projDir = self.opt[self.command.index('--cp')]
        msg = '"{}"'.format(self.opt[self.command.index('-m')])

        os.chdir(f"C:/Users/cpste/Desktop/Projects/{projDir}")
        os.system("git add .")
        os.system(f"git commit -m {msg}")

        if '-f' in self.opt:
            os.system("git push -f")

        else:
            os.system("git push")

    # open a project with IntelliJ
    def open(self):
        os.system(f"{self.intelliJ} {self.projects}/{self.opt}")

    # open a project with PyCharm
    def openPython(self):
        os.system(f"{self.pycharm} {self.projects}/{self.opt}")

    # start wireless debugging
    @staticmethod
    def tcpip():
        os.chdir("C:/Users/cpste/Desktop/platform-tools/")
        os.system("adb tcpip 5555")
        os.system("adb connect 192.168.1.115")

    # disconnect connected devices
    @staticmethod
    def disconnect():
        os.chdir("C:/Users/cpste/Desktop/platform-tools/")
        os.system("adb disconnect")
