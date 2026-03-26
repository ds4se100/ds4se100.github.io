import sys
import re

ARGS = sys.argv

with open(ARGS[1]) as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        if len(line) == 0:
            continue
        tokens = []
        name = line
        while True:
            m = re.search(r'[a-z][A-Z]', name)
            if m is None:
                tokens.append(name.lower())
                break
            tokens.append(name[0:m.start()+1].lower())
            name = name[m.start()+1:]
        print(line, '-->', tokens)
