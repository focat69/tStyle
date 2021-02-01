# ! PLAN !
#Create a theme class which allows you to inject css.
    #It will create a js file which when put into the console,
        #It will inject the css.
from time import sleep
import sys #for checking platform to use clear/cls command
import os #to clear screen

class Theme:
    def __init__(self):
        self.css = ''
        self.cssx = None
        self.styled = False
        self.jsgen = None
        if sys.platform == "win32":
            os.system('cls')
        else:
            os.system('clear')

    def style(self):
        self.lines = int(input('How many lines of css? '))
        self.line = 0
        print("If you have more than 1 object to change, say body and span, then add a space before the next one.\nLine (line): body {\n  ...\n}\n span {...")
        print("^ Put space there. (INDENTATION WILL BE THE SAME)\n\n")
        for i in range(self.lines):
            self.line += 1
            self.cssx = input(f"Line {self.line}: ")
            self.css += self.cssx

        if sys.platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
        
        print(self.css)
        print('\n\nWARNING: ANY FILE WITH THE SAME NAME WILL BE OVERWRITTEN.')
        self.filename = input('CSS file name (no ext, instructions to apply on github)? ')
        print("\nAll done. Generating new css file..")
        sleep(5)
        self.styled = True
        with open(f'{self.filename}.css', 'w') as f:
            f.write(self.css)
        print("Finished.")
        input('Press enter to exit styler.\n')

    def description(self, desc):
        if self.styled:
            print(desc['name'])
            print(desc['author'])
            print(desc['date_made'])
            print(desc['about'])
        else:
            print("Generate the css file first!")