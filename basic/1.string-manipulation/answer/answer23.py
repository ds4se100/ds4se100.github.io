import sys
import re

ARGS = sys.argv

with open(ARGS[1]) as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        if len(line) == 0:
            continue
        matched_tokens = re.findall(r'#\d+|TINKERPOP-\d+', line)
        if len(matched_tokens) == 0:
            continue
        commit = re.match(r'^[0-9a-f]+', line)
        print(commit.group(), matched_tokens)
