import sys

txt_file = sys.argv[1]

with open(txt_file, encoding="utf-8") as f:
    print("行数 =", len(f.readlines()))
