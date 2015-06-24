

import colors as c
from utils import ask

intro = c.blue + '''
Welcome to my Geometry Dash quiz.
Let's test your knowledge...
'''

def q1():
    answer = ask("What is the hardest color to get?")
    if answer == "black":
        print(":)")
        return True
    print(":<")
    return False

def q2():
    answer = ask("What level is the hardest of them all?")
    if answer.startswith("theory of everything 2"):
        print(":)")
        return True
    print(":<")
    return False

def q3():
    answer = ask("Can you use one word to describe how awesome Geomtry dash is?")
    if answer.startswith("epic"):
        print(":)")
        return True
    print(":<")
    return False

questions = [q1,q2,q3]


