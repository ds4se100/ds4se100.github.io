import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("引数で比較する2つのフォルダ名を指定してください")
else:
    folder_name1 = sys.argv[1]
    folder_path1 = Path(folder_name1)
    folder_name2 = sys.argv[2]
    folder_path2 = Path(folder_name2)

    all_files1 = list(folder_path1.glob("**/*"))
    all_files2 = list(folder_path2.glob("**/*"))
    # ファイルのみを抽出
    files1 = {f.name for f in all_files1 if f.is_file()}
    files2 = {f.name for f in all_files2 if f.is_file()}
    
    # 重複していないファイルを取得
    unique_to_folder1 = files1 - files2
    unique_to_folder2 = files2 - files1
    
    print(f"{folder_name1} にのみ存在するファイル:")
    for file_name in sorted(unique_to_folder1):
        print(f"  {file_name}")
    
    print(f"\n{folder_name2} にのみ存在するファイル:")
    for file_name in sorted(unique_to_folder2):
        print(f"  {file_name}")
