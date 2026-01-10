import sys
from pathlib import Path

prefix = "mark_"

if len(sys.argv) != 2:
    print("引数でフォルダ名を指定してください")
else:
    folder_name = sys.argv[1]
    folder_path = Path(folder_name)

    for file in folder_path.iterdir():
        if file.is_file():
            new_name = prefix + file.name
            new_path = file.parent / new_name
            file.rename(new_path)
