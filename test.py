import re

REGEXES = [
    r".* left the group"
]

HAYSTACK = [
    "ZyleGeralde de la Pena left the group.",
]

for stack in HAYSTACK:
    print(f"stack is: {stack}")
    for regx in REGEXES:
        if re.match(regx,stack):
            print("Success")
        else:
            print("fail")
