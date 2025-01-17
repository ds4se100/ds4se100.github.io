[【トップページへ戻る】](../)

# 関数名を解析する

## はじめに

この課題では，Python ソースファイルの集合を対象とし，
そこで登場する関数名の簡単な解析を目的としている．

以下では
https://github.com/tornadoweb/tornado
で公開されている Git リポジトリ（タグ v6.4.2）を解析対象とする．

（参考：取得方法）
```sh
git clone https://github.com/tornadoweb/tornado  
cd tornado
git checkout v6.4.2
```


<!-- （この ZIP ファイルには複数の Python ソースファイル（.py ファイル）が階層的に格納されている．まずはこれをダウンロードして，自分の環境で展開し，以下の問に答えよ．）  
与えられたフォルダに含まれるすべての Python ソースファイルに対し，それらのファイルの中で定義されている関数名（クラス内のメソッド名を含む）をすべて抽出せよ．  
そして，各関数名の先頭に使われているトークンに注目し，それらを出現頻度ともに（頻度の降順に並べて）出力せよ．あわせて，英単語でないものについては * 印を付けて出力せよ． -->


---
## （関数名の分割） 4.1 -- 4.4

### 4.1
複数の文字列（ただし，英数字のみ使用可）をアンダースコアでつなげた表記法をスネークケースと呼ぶ．  

スネークケースで書かれた関数名（文字列）が与えられたとき，それを構成するトークン（単語等）をすべて抽出せよ．ただし，空文字列（長さ0）はトークンとは見なさない．

（例）
- `'get_file_name'` --> `['get', 'file', 'name']`
- `'__foo_bar_'` --> `['foo', 'bar']`

---
### 4.2 

英数字のみで構成された関数名（文字列）が与えられたとき，
数字を区切り文字としてそれを分割せよ．
ただし，数字は 1 桁とは限らない．また，空文字列（長さ0）はトークンとは見なさない．

（例）
- `'bin2hex'` --> `['bin', 'hex']`
- `'encode2base64'` --> `['encode', 'base']`
- `'base64str'` --> `['base', 'str']`

---
### 4.3 

スネークケースでは複数のトークンをアンダースコアでつなげて書くが，アンダースコアを使う代わりに 2 番目以降のトークンの先頭文字を大文字にすることでトークンの区切りを表す表記法をキャメルケースと呼ぶ．

キャメルケースで書かれた関数名が与えられたとき，それを構成するトークンをすべて抽出せよ．

（例）
- `'getFileName'` --> `['get', 'File', 'Name']`
- `'loadJSON'` --> `['load', 'JSON']`

---
### 4.4 

関数名が与えられたとき，それを構成するトークンをすべて抽出せよ．
ただし，関数名の表記法としてスネークケースとキャメルケースが混在していてもよいものとする．
あわせて，数字もトークンの区切りと見なす．

（例）
- `'get_file_name'` --> `['get', 'file', 'name']`
- `'getFileName'` --> `['get', 'File', 'Name']`
- `'dataDict2JSON_file'` --> `['data', 'Dict', 'JSON', 'file']`


---
## （フォルダの走査） 4.5 -- 4.6

### 4.5

与えられたフォルダに格納されている Python ソースファイルの個数を答えよ．

（実行例：作成したファイル名を p0405.py として）
```sh
python p0405.py tornado
Python ソースファイル数 = 108
```

---
### 4.6 

与えられたフォルダに格納されている Python ソースファイルの絶対パスの一覧を作成せよ．ただし，一覧は絶対パスの辞書順に並べるものとする．

（実行例：作成したファイル名を p0406.py とし，実行ディレクトリを /Users/xxx として）
```sh
python p0406.py tornado  
/Users/xxx/tornado/demos/blog/blog.py
/Users/xxx/tornado/demos/chat/chatdemo.py
/Users/xxx/tornado/demos/facebook/facebook.py
...
/Users/xxx/tornado/tornado/web.py
/Users/xxx/tornado/tornado/websocket.py
/Users/xxx/tornado/tornado/wsgi.py
```

---
## （抽象構文木（AST）解析） 4.7 -- 4.8
### 4.7

与えられた Python ソースファイルに対し，Python の ast モジュールで提供されている構文解析機能（ast.parse, ast.dump）を使って AST を画面に出力せよ．

（例）
- 解析対象の Python プログラム
```
def computeFact(n):
    if n < 2:
        return 1
    return n * computeFact(n-1)

print( fact(5) )
```

- ast.dump で出力される AST データ（``indent=2`` を指定した場合）
```
Module(
  body=[
    FunctionDef(
      name='computeFact',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(arg='n')],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        If(
          test=Compare(
            left=Name(id='n', ctx=Load()),
            ops=[
              Lt()],
            comparators=[
              Constant(value=2)]),
          body=[
            Return(
              value=Constant(value=1))],
          orelse=[]),
        Return(
          value=BinOp(
            left=Name(id='n', ctx=Load()),
            op=Mult(),
            right=Call(
              func=Name(id='computeFact', ctx=Load()),
              args=[
                BinOp(
                  left=Name(id='n', ctx=Load()),
                  op=Sub(),
                  right=Constant(value=1))],
              keywords=[])))],
      decorator_list=[],
      type_params=[]),
    Expr(
      value=Call(
        func=Name(id='print', ctx=Load()),
        args=[
          Call(
            func=Name(id='computeFact', ctx=Load()),
            args=[
              Constant(value=5)],
            keywords=[])],
        keywords=[]))],
  type_ignores=[])
```


- ast.dump で出力される AST データ（``indent`` を指定しない場合）
```
Module(body=[FunctionDef(name='computeFact', args=arguments(posonlyargs=[], args=[arg(arg='n')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Name(id='n', ctx=Load()), ops=[Lt()], comparators=[Constant(value=2)]), body=[Return(value=Constant(value=1))], orelse=[]), Return(value=BinOp(left=Name(id='n', ctx=Load()), op=Mult(), right=Call(func=Name(id='computeFact', ctx=Load()), args=[BinOp(left=Name(id='n', ctx=Load()), op=Sub(), right=Constant(value=1))], keywords=[])))], decorator_list=[], type_params=[]), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Call(func=Name(id='computeFact', ctx=Load()), args=[Constant(value=5)], keywords=[])], keywords=[]))], type_ignores=[])
>>> 
```

### 4.8 

（問 4.7 で出力した） AST データ（``indent`` を指定しない場合）が文字列として与えられたとき，その中に登場する `FunctionDef(name='xxx'` という文字列をすべて検索し，関数名を抽出せよ．ただし，関数名は `xxx` という部分が該当する．


（実行例：作成したファイル名を p0408.py として）
```sh
python p0408.py tornado/tornado/log.py
['_stderr_supports_color', '_safe_unicode', '__init__', 'format', 'enable_pretty_logging', 'define_logging_options']
```
<!-- ### 4.9
問 4.8 で得られた関数名をトークンへ分割し，先頭のトークンのみを抽出せよ．

（例）問4.8 の場合  
`[ 'compute' ]` -->

---
## （関数名の品詞解析） 4.9 -- 4.11
### 4.9
与えられた英文（文字列）を nltk の word_tokenize 関数を用いてトークン列に分割しなさい。
そして、同じく nltk で提供されている pos_tag 関数を用いて品詞列を出力しなさい．

（例）
- トークン列：`'This is a sample sentence for tokenization.'` --> `['This', 'is', 'a', 'sample', 'sentence', 'for', 'tokenization', '.']`
- 品詞列：`'['This', 'is', 'a', 'sample', 'sentence', 'for', 'tokenization', '.']'` --> `'['DT', 'VBZ', 'DT', 'JJ', 'NN', 'IN', 'NN', '.']'`

---
### 4.10
与えられた関数名を問 4.4 に従ってトークン列に分割し（nltk ではない点に注意），
それらの品詞列を nltk で提供されている pos_tag 関数でもって調べなさい．

（例）
- `'get_file_name'` --> `('VB', 'NN', 'NN')`

---
### 4.11
指定されたフォルダ内に含まれる全 Python ソースファイルを対象とし，
それらに登場するすべての関数名を抽出しなさい．  
そして，各関数名について品詞列（問 4.10 参照）を求め，品詞列の出現頻度を高い順に出力しなさい．  
ただし，出力するのは上位 5 件までとする．

（例）
```
1位: ['NN'](644回）
2位: ['NN', 'NN'](340回）
3位: ['VB'](232回）
4位: ['NN', 'NN', 'NN'](231回）
5位: ['VB', 'NN'](124回）
```

---
### 解答例
[解答例はこちら](./answer.html){:target="_blank"} /
[ipynbファイルをダウンロード](./answer.ipynb)
