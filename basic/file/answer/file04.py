import sys
import pandas as pd

csv_file = sys.argv[1]
df = pd.read_csv(csv_file)

for cls in list(set(df['class'])):
    df_sub = df[df['class']==cls]
    df_sub = df_sub.drop(columns='class')
    df_sub.to_csv(cls+'.csv', index=False)

