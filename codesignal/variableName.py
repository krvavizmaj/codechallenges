import re

def variableName(name):
    return bool(re.match(r'^[a-z,A-Z]+[a-z,A-Z,\d,_]*$', name))

print(variableName("abd_33"))