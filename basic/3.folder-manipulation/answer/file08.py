import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("引数でフォルダ名とファイル名を指定してください")
else:
    folder_name = sys.argv[1]
    folder_path = Path(folder_name)
    file_name = sys.argv[2]

    all_files = list(folder_path.glob("**/*"))
    found_files = []
    for file in all_files:
        if file.is_file() and file.name == file_name:
            found_files.append(file)
    
    if found_files:
        for found_file in found_files:
            print(found_file)
    else:
        print(f"ファイル '{file_name}' が見つかりませんでした")
