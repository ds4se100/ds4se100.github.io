import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("引数でフォルダ名を指定してください")
else:
    folder_name = sys.argv[1]
    folder_path = Path(folder_name)

    for file in folder_path.iterdir():
        print(f"{file.name}")
