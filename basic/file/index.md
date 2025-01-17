[【トップページへ戻る】](../../)

# **ファイル処理**

### (1) **テキストファイルの行数**
この[テキストファイル（wws2025cfp.txt）](./data/wws2025cfp.txt)について，その行数を出力するプログラムを作りなさい．

- 実行例（作成したプログラムを ```file01.py``` として）
```shell-session
$ python file01.py wws2025cfp.txt
行数 = 15
```

### (2) **テキストファイルを行番号付きで**
この[テキストファイル（wws2025cfp.txt）](./data/wws2025cfp.txt)について，その内容を行番号付きで出力するプログラムを作りなさい．

- 実行例（作成したプログラムを ```file02.py``` として）
```shell-session
$ python file02.py wws2025cfp.txt
 1 : 近年，産業界・学界を問わず「データサイエンス」が注目を集めている．
 2 : もともとは統計分析とデータマイニングを基盤として発展した分野であるが，
 3 : 最近では機械学習や AI 技術も活用したより高度なものになってきている．
 4 : ソフトウェア工学分野でもこれらを活用した研究や取り組みは多く，多岐に渡る．
 5 : これに関連して，研究者や技術者が学ぶべき内容も多様化してきており， 適切な教材に対するニーズは高まっている．
 6 :
 7 : 本セッションではソフトウェア工学分野におけるデータの分析や活用に関する基礎技術を学ぶための教材として
 8 : 「ソフトウェア工学のためのデータサイエンス 100 本ノック（仮称）」 を構築する共同作業の場を提供したい．
 9 :
10 : 教材の主なテーマとしては，バグ予測，品質評価・改善，見積り，リポジトリマイニング，
11 : その他データサイエンス・AIのソフトウェア開発・保守への応用などを想定しているがこれらに限定されるものではない．
12 : ワークショップでは教材の提案や共同開発，並びに内容のレビューに協力 いただける方の参加を期待している．
13 : 教材に対するニーズの検討や適切な難易度設定という観点から，初学者（学生の方を含む）の参加も歓迎する．
14 : なお，作業では GitHub を使用するため，申し込みの際には可能ならばご自身の GitHub アカウントをお知らせいただきたい．
15 : （議論のみ参加も認めるため，アカウントは必須ではありません．）
```

### (3) **CSVファイルのヘッダーと行数**
この[CSV ファイル（カンマ区切りファイル）(iris.csv)](./data/iris.csv)について，
- データの行数，
- 1 行目（ヘッダー）に書かれている項目数，
- 項目の一覧，

を出力するプログラムを作りなさい．  
ただし，データの行数にはヘッダー（1行目）は含めないものとする．  
（※ iris データの配布元 [https://archive.ics.uci.edu/dataset/53/iris](https://archive.ics.uci.edu/dataset/53/iris){:target="_blank"}）

- 実行例（作成したプログラムを ```file03.py``` として）
```shell-session
$ python file03.py iris.csv
行数 = 150
項目数 = 5
項目1：sepal_length
項目2：sepal_width
項目3：petal_length
項目4：petal_width
項目5：class
```

### (4) **CSVファイルの読み書き（データの抽出を含む）** 
この[CSV ファイル（カンマ区切りファイル）(iris.csv)](./data/iris.csv)に格納されているデータででは，
class として 'Iris-setosa', 'Iris-versicolor', 及び 'Iris-virginica' の 3 種類がある．  
このデータを class ごとに分けて 3 つの CSV ファイルへそれぞれ出力するプログラムを作りなさい．  
なお，出力先の CSV ファイル名は「クラス名」+「.csv」とし，それぞれのデータ列 class は含めないものとする．

 実行例（作成したプログラムを ```file04.py``` として）
```shell-session
$ python file04.py iris.csv
```

実行後，3 つのファイル（[Iris-setosa.csv](./data/Iris-setosa.csv), [Iris-versicolor.csv](./data/Iris-versicolor.csv), [Iris-virginica.csv](./data/Iris-virginica.csv)）が作られることになる．


### (5) **JSONファイルの読み込み**
この[JSON ファイル(iris.json)](./data/iris.json)を読み込んで，格納されているデータ数と各データの内容を出力するプログラムを作りなさい．  
ただし，このJSONファイルでは 150 個のデータが配列（リスト）のかたちで与えられており，各データは辞書型になっている．

 実行例（作成したプログラムを ```file05.py``` として）
```shell-session
$ python file05.py iris.json
データ数 = 150
データ001
{'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'class': 'Iris-setosa'}
データ002
{'sepal_length': 4.9, 'sepal_width': 3.0, 'petal_length': 1.4, 'petal_width': 0.2, 'class': 'Iris-setosa'}
...
... （途中省略）
...
データ150
{'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'class': 'Iris-virginica'}
```

### **解答例**
注意：プログラムにエラー処理等は入れていません．

|問題|解答例プログラム|
|:-------------|:------------------|
|(1) テキストファイルの行数|[file01.py](./answer/file01.py)|
|(2) テキストファイルを行番号付きで|[file02.py](./answer/file02.py)|
|(3) CSVファイルのヘッダーと行数|[file03.py](./answer/file03.py)|
|(4) CSVファイルの読み書き（データの抽出を含む）|[file04.py](./answer/file04.py)|
|(5) JSONファイルの読み込み|[file05.py](./answer/file05.py)|

