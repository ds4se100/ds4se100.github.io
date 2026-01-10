import sys
from pathlib import Path
import hashlib

if len(sys.argv) != 2:
    print("引数でフォルダ名を指定してください")
else:
    folder_name = sys.argv[1]
    folder_path = Path(folder_name)

    all_files = list(folder_path.glob("**/*"))
    file_hashes = {}
    
    for file in all_files:
        if file.is_file():
            with open(file, 'rb') as f:
                content = f.read()
                hash_value = hashlib.md5(content).hexdigest()
                
            if hash_value not in file_hashes:
                file_hashes[hash_value] = []
            file_hashes[hash_value].append(file)
    
    for hash_value, files in file_hashes.items():
        print(f"ハッシュ値: {hash_value}")
        for file in files:
            print(f"  {file}")


