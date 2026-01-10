import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("引数でフォルダ名とファイル名を指定してください")
else:
    folder_name = sys.argv[1]
    folder_path = Path(folder_name)
    file_name = sys.argv[2]

    for f in folder_path.iterdir():
        if f.is_file() and f.name == file_name:
            print(f)
            break
    else:
        print(f"ファイル '{file_name}' が見つかりませんでした")
