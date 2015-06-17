"""This is my EPIC tool box of STUFS. And don't you DARE judge me!"""

import colors as c

def ask(qustion):
    print(c.yellow + qustion + c.reset)
    anwser = input("> " + c.base3).lower().strip()
    print(c.reset)
    return anwser

if __name__ == '__main__':
    print(c.clear)
    name = ask("What is your name?")
    color = ask("What is your name in color?",c.random_color())
