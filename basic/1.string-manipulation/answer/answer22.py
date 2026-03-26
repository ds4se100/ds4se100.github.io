import sys
import re

ARGS = sys.argv

with open(ARGS[1]) as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        if len(line) == 0:
            continue
        if re.search(r'#\d+|TINKERPOP-\d+', line):
            print(line)
