
[【トップページへ戻る】](../../)

# 基本編7: データ分析・機械学習系

## 71. ファイルのダウンロード
[リンク先](https://www.kaggle.com/datasets/toniesteves/desharnais-dataset?resource=download)から `02.desharnais.csv` をダウンロードしなさい．ただし，アカウント作成の必要がある．

## 72 新たなメトリクスの作成
`02.desharnais.csv` のEffortとLengthから生産性を表す新たなメトリクスproductivityを作成しなさい．

## 73. データのクレンジング
`02.desharnais.csv` に含まれるカテゴリカルデータのダミー変数化，および，欠損値(データセット中の-1)をリストワイズ除去法で除去し，データ分析可能なデータセットに整形しなさい．

## 74. データの可視化
整形後のデータセットの各メトリクス間の関係を散布図行列を用いて可視化しなさい．

## 75. 分析モデルの作成
整形後のデータセットから生産性を目的変数として線形重回帰モデルを作成しなさい．

## 76.  モデルのチューニング
作成した線形重回帰モデルについて，ステップワイズ変数選択により変数選択を行った線形重回帰モデルを作成しなさい．

## 77. 予測
変数選択後の線形重回帰モデルを用いて，生産性の予測値を算出し，実測値との相対誤差を求めなさい．

## 78. 高精度予測メトリクスの作成
高精度（相対誤差が20%未満）で予測できたケースを表す新たなメトリクスを作成しなさい．

## 79. 判別モデルの作成
線形重回帰分析により高精度で予測できるかを判別するモデルをランダムフォレストで作成しなさい．ただし，モデル作成のための訓練データは63件とし，残りは判別精度を求めるためのテストデータとすること．

## 80. 判別モデルの評価
テストデータの判別結果より，混同行列を作成し適合率と再現率を求め，また，ROC曲線を示し，作成したモデルを評価しなさい．
