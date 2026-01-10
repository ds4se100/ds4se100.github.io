import sys
from pathlib import Path
import datetime

if len(sys.argv) != 2:
    print("引数でフォルダ名を指定してください")
else:
    folder_name = sys.argv[1]
    folder_path = Path(folder_name)

    for file in folder_path.iterdir():
        if file.is_file():
            file_age = datetime.datetime.now() - datetime.datetime.fromtimestamp(file.stat().st_mtime)
            file_size = file.stat().st_size
            
            if file_age.days >= 30 or file_size < 1000:
                print(f"{file.name}")
