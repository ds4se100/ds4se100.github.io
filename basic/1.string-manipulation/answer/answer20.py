import sys

ARGS = sys.argv

with open(ARGS[1]) as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        if len(line) == 0:
            continue
        tokens = [ tk for tk in line.split('_') if len(tk) > 0 ]
        print(line, '-->', tokens)
