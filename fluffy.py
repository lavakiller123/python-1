

import colors as c
from utils import ask

intro = c.magenta + '''
Welcome to the Pink Fluffy Unicorns quiz.
Let's test your knowledge...
'''

def q1():
    answer = ask("What color are the unicorns?")
    if answer == "pink":
        print(":)")
        return True
    print(":<")
    return False

def q2():
    answer = ask("What are the unicorns dancing on?")
    if answer.startswith("rainbow"):
        print(":)")
        return True
    print(":<")
    return False

def q3():
    answer = ask("Use one word to describe the texture of their magical fur?")
    if answer.startswith("smile"):
        print(":)")
        return True
    print(":<")
    return False

questions = [q1,q2,q3]


