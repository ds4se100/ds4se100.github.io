
[【トップページへ戻る】](../../)

# 基本編3: フォルダ（ディレクトリ）処理

各課題は、主に `sys` モジュールや `pathlib` モジュールなどを使用して解くことを想定しています。

### 31. フォルダの作成と確認
指定した名前のフォルダを新規作成し、そのフォルダが既に存在している場合は「存在します」と表示する処理を書いてください。

- 実行例（作成したプログラムを ```file01.py``` として）
```shell-session
$ ls -a
.	..
$ python file01.py folder01
$ ls -a
.	..	folder01
```

### 32. ファイル一覧の取得
特定のフォルダ内にあるすべてのフォルダ名およびファイル名を取得して一覧表示してください。

- 実行例（作成したプログラムを ```file02.py``` として）
```shell-session
$ ls folder02
a.txt		b.csv		c.txt		subfolder01
$ python file02.py folder02
a.txt
b.txt
c.txt
subfolder01
```

### 33. 拡張子によるフィルタリング
特定のフォルダ内から「.csv」ファイルだけを抽出して、その絶対パスを一覧表示してください。

- 実行例（作成したプログラムを ```file03.py``` として）
```shell-session
$ ls folder03
a.txt		b.csv		c.txt		subfolder01
$ python file03.py folder03
/home/user01/folder03/b.csv
```

### 34. 複数の条件によるフィルタリング
特定のフォルダ内から、修正から30日以上経過した古いファイル、またはファイルサイズが 1000 バイト未満のファイルだけを抽出して、そのファイルパスを一覧表示してください。

- 実行例（作成したプログラムを ```file04.py``` として）
```shell-session
$ ls -l folder04
total 24
-rw-r--r--  1 user01  staff  1102  1 10 09:27 a.txt
-rw-r--r--  1 user01  staff   468  1 10 09:28 b.csv
-rw-r--r--  1 user01  staff  1269 11 10 07:00 c.txt
drwxr-xr-x  2 user01  staff    64  1 10 09:23 subfolder01
$ python file04.py folder04
b.csv
c.txt
```

### 35 一括リネーム
フォルダ内のすべてのファイル名の先頭に、接頭辞（例：mark_）を付与してリネームしてください。

- 実行例（作成したプログラムを ```file05.py``` として）
```shell-session
$ ls folder05
a.txt		b.csv		c.txt		subfolder01
$ python file05.py folder05
$ ls folder05
mark_a.txt		mark_b.csv		mark_c.txt		subfolder01
```

### 36 連番の付与
フォルダ内のすべてのファイルをファイル名で昇順にソートして、連番の接頭辞（例：0001_）を付与してください。

- 実行例（作成したプログラムを ```file06.py``` として）
```shell-session
$ ls folder06
a.txt		b.csv		c.txt		subfolder01
$ python file06.py folder06
$ ls folder06
0001_a.txt		0002_b.csv		0003_c.txt		subfolder01
```

### 37 ファイル探索
指定したフォルダの中から指定したファイル名のファイルをすべて検索して相対パスを表示してください。

- 実行例（作成したプログラムを ```file07.py``` として）
```shell-session
$ ls folder07
a.txt		b.csv		c.txt		subfolder01
$ python file07.py folder07 c.txt
folder07/c.txt
```

### 38 再帰的なファイル探索
指定したフォルダだけでなく、その中にある「サブフォルダ」の中身まで含めて、すべてのファイルを検索してください。

- 実行例（作成したプログラムを ```file07.py``` として）
```shell-session
$ tree folder08
folder08
├── a.txt
├── b.csv
├── c.txt
└── subfolder01
    └── c.txt

2 directories, 4 files

$ python file08.py folder08 c.txt
folder08/c.txt
folder08/subfolder01/c.txt
```

### 39. 重複ファイルの特定
指定したフォルダの中から、ファイル名が異なっても「内容が全く同じ」ファイルをハッシュ値（MD5など）を使って見つけ出し、重複しているものを表示してください。

- 実行例（作成したプログラムを ```file09.py``` として）
```shell-session
$ ls -l folder09
total 24
-rw-r--r--  1 user01  staff  1102  1 10 10:25 a.txt
-rw-r--r--  1 user01  staff  1102  1 10 10:25 b.txt
-rw-r--r--  1 user01  staff  1269  1 10 10:25 c.txt
-rw-r--r--  1 user01  staff  1269  1 10 10:25 d.txt
$ python file09.py folder09
ハッシュ値: d9a961ab95ddbbc894d00b9d456523da
  folder09/c.txt
  folder09/d.txt
ハッシュ値: 65cae1379beae3d3d00429cc7bdf8f04
  folder09/b.txt
  folder09/a.txt
```

### 40 フォルダの差分
指定した2つのフォルダに含まれるファイル名の差分を表示してください。いずれのフォルダ内にもサブフォルダはないものとします。

- 実行例（作成したプログラムを ```file10.py``` として）
```shell-session
$ ls folder10_1 folder10_2
folder10_1:
a.txt	b.txt	c.txt	d.txt

folder10_2:
a.txt	b.csv	c.txt

$ python file10.py folder10_1 folder10_2 
folder10_1 にのみ存在するファイル:
  b.txt
  d.txt

folder10_2 にのみ存在するファイル:
  b.csv
```

