import sys
import json

json_file = sys.argv[1]

with open(json_file) as f:
    data = json.load(f)

print('データ数 =', len(data))
for idx, items in enumerate(data):
    print('データ{:03d}'.format(idx+1))
    print(items)