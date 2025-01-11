import sys

txt_file = sys.argv[1]

with open(txt_file, encoding="utf-8") as f:
    all_lines = f.readlines()

    # 行数の桁数を調べる（行番号の表示幅を決めるため）
    digits = 1
    while (10**digits < len(all_lines)):
        digits += 1

    for num, line in enumerate(all_lines):
        # line には行末に改行文字も含まれるため，
        # print では行末の改行は行わない．
        print(str(num+1).rjust(digits), ':', line, end='')
