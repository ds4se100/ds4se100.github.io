[【トップページへ戻る】](../../)

# 基本編1: 文字列処理

## 11. 文字列の置換
ある学生の学籍番号EN26CS0337からen26cs0337@softwareknock.eduというメールアドレスを作成したい．
学籍番号の大文字を小文字に置換する，すなわちEN26CS0337をen26cs0337に変換して出力しなさい．

## 12. 文字列の結合
en26cs0337の後ろに@softwareknock.eduを追加し，メールアドレスen26cs0337@softwareknock.eduを作成して出力しなさい

## 13. 文字列の抽出 1
EN17CS0337から数字だけを抽出した170337という文字列をis.digit()を使って作成・出力しなさい．

## 14. 文字列の抽出 2
13. をis.digit()を使わずに，すなわちEN17CS0337から数字である3-4文字目，7-10文字目を抽出・結合し，170337という文字列を作成・出力しなさい．

## 15. 文字列の抽出 3
13., 14. の処理を正規表現を用いて行いなさい

## 16. チェックディジット（数値）の付加
170337の「末尾に」1桁の数字を加えて，9で割り切れるようにしなさい

## 17. チェックディジット（文字）の付加
16. と同じ作業を，今度は11で割り切れるようにしなさい．ただし末尾はアルファベットと用いるものとして，数字とアルファベットの対応表は以下の通りである．

|A|B|C|H|K|M|R|U|X|Y|Z|
|----|----|----|----|----|----|----|----|----|----|----|
|0|1|2|3|4|5|6|7|8|9|10|

## 18. チェックディジット（数値）の検査
2733376が9で割り切れるか確認し，確認できれば「9で割り切れる」，できなければ「9で割り切れない」と回答しなさい

## 19. チェックディジット（文字）の検査
273377Cが11で割り切れるか確認し，確認できれば「11で割り切れる」，できなければ「11で割り切れない」と回答しなさい．アルファベットと数字の対応表は 17. と同様とする．


## 20. 文字列の分割（特定の文字で分割）

この[テキストファイル（snake_case_data.txt）](./data/snake_case_data.txt)には，1 行に 1 つずつ文字列が書いてある．  
ただし，各文字列には 1 つ以上の英単語や略語が使われており，単語・略語の区切りにはアンダースコア（`_`）が使われている．  
これを読み込み，文字列を分割して出力するプログラムを作りなさい．

- 実行例（作成したプログラムを ```xxx.py``` として）
```shell-session
$ python xxx.py snake_case_data.txt
user_id --> ['user', 'id']
password --> ['password']
MAX_DATA_LENGTH --> ['MAX', 'DATA', 'LENGTH']
__init_data__ --> ['init', 'data']
```

（参考）変数名や関数名に複合語（複数の単語をつなげたもの）を使う場合，単語をアンダースコアでつないで書く記法を**スネークケース**や**アンダースコア**という．


## 21. 正規表現にマッチする行を出力

この[テキストファイル（git_log_data.txt）](./data/git_log_data.txt)には，オープンソースソフトウェアの Git リポジトリから取得したコミットログの一部が格納されている．  
内容は，1 行が 1 つのコミットに対応しており，コミットハッシュとコミットメージがそれぞれ書かれている．  
これを読み込み，```#```とそれに続く 1 桁以上の整数（例えば ```#123```）が登場する行のみを出力するプログラムを作りなさい．

- 実行例（作成したプログラムを ```xxx.py``` として）
```shell-session
$ python xxx.py git_log_data.txt
61c37a1e24 Integrate JavaScript examples into CI build (#3240)
234d578028 TINKERPOP-3218 Fix bug in pre-repeat emit()/until() (#3288)
53959cc41c TINKERPOP-3217 Add server option to close Session automatically. (#3284)
4f88964daa TINKERPOP-3213 Add SessionedChildClient (#3258)
```

## 22. 複数の正規表現のいずれかにマッチする行を出力

上と同様に特定のパターンにマッチする行のみを出力するプログラムを作りなさい．  
ただし，ここでは注目するパターンとして「```#``` とそれに続く整数」だけでなく
「```TINKERPOP-``` とそれに続く整数」でもよいものとする．

- 実行例（作成したプログラムを ```xxx.py``` として）
```shell-session
$ python xxx.py git_log_data.txt
0f90b39e03 TINKERPOP-3223 Fixed bug in SubgraphStrategy
61c37a1e24 Integrate JavaScript examples into CI build (#3240)
234d578028 TINKERPOP-3218 Fix bug in pre-repeat emit()/until() (#3288)
53959cc41c TINKERPOP-3217 Add server option to close Session automatically. (#3284)
4f88964daa TINKERPOP-3213 Add SessionedChildClient (#3258)
```

## 23. 正規表現にマッチする部分を抽出

上と同様に，注目する 2 種類のパターンのいずれかにマッチする部分のみ（*行全体ではない*）を出力するプログラムを作りなさい．  
ただし，行頭のコミットハッシュも一緒に出力することとする．  
なお，コミットハッシュは 16 進のコード（[0-9a-f]の並び）である．

- 実行例（作成したプログラムを ```xxx.py``` として）
```shell-session
$ python xxx.py git_log_data.txt
0f90b39e03 ['TINKERPOP-3223']
61c37a1e24 ['#3240']
234d578028 ['TINKERPOP-3218', '#3288']
53959cc41c ['TINKERPOP-3217', '#3284']
4f88964daa ['TINKERPOP-3213', '#3258']
```

## 24. 文字列の分割（正規表現にマッチする位置で分割）

この[テキストファイル（camel_case_data.txt）](./data/camel_case_data.txt)には，1 行に 1 つずつ文字列が書いてある．  
ただし，各文字列には 1 つ以上の英単語や略語が使われており，単語・略語は**キャメルケース**（単語の区切りを大文字で始める記法）で書かれている．
これを読み込み，文字列を分割して出力するプログラムを作りなさい．  
なお，分割後の文字列は*すべて小文字に*すること．

- 実行例（作成したプログラムを ```xxx.py``` として）
```shell-session
$ python xxx.py camel_case_data.txt
userId --> ['user', 'id']
password --> ['password']
maxDataLength --> ['max', 'data', 'length']
DataType --> ['data', 'type']
```

---
## 解答例

|問題|解答例プログラム|
|:-------------|:------------------|
|11--19|[Jupyter Notebook 形式で表記](./answer/basic_1_answer.md)|
|20--24|準備中|

