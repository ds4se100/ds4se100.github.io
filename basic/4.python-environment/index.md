[【トップページへ戻る】](../../)

# 基本編4: 仮想環境（Python）

## 41. 特定versionのpythonの環境を作る
特定versionのpython環境を作成しなさい．また，それとは異なるversionのpython環境を作成しなさい．

- 実行例 
```shell-session
# python version確認
$ python --version
Python 3.8.0

# python versionを変更するコマンド

# python version確認
$ python --version
Python 3.10.0
```

## 42. 特定バージョンのライブラリをインストール
最新版ではない特定バージョンのpythonライブラリをインストールして，そのバージョンがインストールされたことを確認しなさい．
（発展: githubで公開されているpythonライブラリの特定コミット時点のものをインストールしなさい．例: https://github.com/tweepy/tweepy）

- 実行例（作成したプログラムを ```file02.sh``` として）
```shell-session
$ source file02.sh
...
Successfully installed {library}-{version}
```
