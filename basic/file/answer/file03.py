import sys
import pandas as pd

csv_file = sys.argv[1]
df = pd.read_csv(csv_file)

print('行数 =', len(df))
print('項目数 =', len(df.columns))

for i, col in enumerate(df.columns):
    print('項目{}：{}'.format(i+1, col))

