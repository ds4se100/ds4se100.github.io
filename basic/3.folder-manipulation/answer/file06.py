import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("引数でフォルダ名を指定してください")
else:
    folder_name = sys.argv[1]
    folder_path = Path(folder_name)

    files = [f for f in folder_path.iterdir() if f.is_file()]
    files.sort(key=lambda x: x.name)
    
    for i, file in enumerate(files, 1):
        new_name = f"{i:04d}_{file.name}"
        new_path = file.parent / new_name
        file.rename(new_path)
