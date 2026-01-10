# 6. 構文解析とメトリクス

1. 与えられた単一のJavaソースファイルを構文解析せよ．

2. 与えられたJavaソースファイルに含まれるすべてのクラス/モジュール$`C`$，メソッド/関数$`M`$，フィールド/属性$`F`$を列挙せよ．

3. 与えられたメソッドの[循環的複雑度](https://ja.wikipedia.org/wiki/循環的複雑度)（サイクロマチック複雑度; Cyclomatic complexity）を計測せよ．
- T.J. McCabe: "[A Complexity Measure](http://www.literateprogramming.com/mccabe.pdf)". IEEE Trans. Softw. Eng. SE-2(4) 308-320, 1976. DOI:[10.1109/TSE.1976.233837](https://doi.org/10.1109/TSE.1976.233837)
循環的複雑度は，制御フロー上の分岐点の個数として求めることができる．

4. 与えられたクラスのWMC（Weighted Methods per Class）を計測せよ．
WMC はクラスに所属するメソッドの複雑さ重みの和として計算される．
メソッドの複雑さ重みには循環的複雑度を用いよ．
- S.R. Chidamber , C.F. Kemerer: "[A Metrics Suite for Object Oriented Design](http://www.pitt.edu/~ckemerer/CK%20research%20papers/MetricForOOD_ChidamberKemerer94.pdf)". IEEE Trans. Softw. Eng. 20(6) 476-493, 1994. DOI:[10.1109/32.295895](https://doi.org/10.1109/32.295895)
- 書籍[Object-Oriented Metrics in Practice](https://doi.org/10.1007/3-540-39538-5)では，"The sum of the statical complexity of all methods of a class. The CYCLO metric is used to quantify the method's complexity"と定義されている．

5. メソッドと，メソッドが使用するフィールドの間の利用関係$`\mathit{use} : M \times F`$を抽出せよ．

6. 与えられたクラスの TCC（Tight Class Cohesion）を計測せよ．
TCCは凝集度のメトリクスのひとつで，対象クラス内のすべてのメソッド対のうち，同クラスの特定のフィールドに共通してアクセスするものの割合を表す．
- 書籍[Object-Oriented Metrics in Practice](https://doi.org/10.1007/3-540-39538-5)では，"The relative number of method pairs of a class that access in common at least one attribute of the measured class"と定義されている．

7. 与えられたプロジェクトディレクトリに含まれる全てのJavaソースファイルを一括で解析し，プログラム要素間の参照関係を特定せよ．
それを用いて，メソッド間の呼出し関係$`\mathit{invoke} : M \times M`$を抽出せよ．

8. 与えられたメソッドがアクセサメソッド（getter/setter）かどうか判定せよ．

9. 与えられたクラスのATFD（Access To Foreign Data）を計測せよ．
ATFDは，対象クラスから（アクセサメソッドによる間接アクセスも含めて）アクセスしている外部クラスのフィールド数を表す．
- 書籍[Object-Oriented Metrics in Practice](https://doi.org/10.1007/3-540-39538-5)では，"The number of attributes from unrelated classes that are accessed directly or by invoking accessor methods"と定義されている．

10. 与えられたクラスが不吉な臭いGod Classを持つかを判定せよ．
書籍[Object-Oriented Metrics in Practice](https://doi.org/10.1007/3-540-39538-5)によるメトリクスベースの判定戦略によれば，下記を条件をすべて満たすクラスをGod Classとみなす．
- `ATFD > FEW` (= 5) (Class uses directly more than a few attributes of other classes)
- `WMC >= VERY HIGH` (= 47) (Functional complexity of the class is very high)
- `TCC < 1/3` (Class cohesion is low)

閾値には`FEW = 5`，`VERY HIGH = 47`を用いよ．
静的解析ツール[PMD](https://pmd.github.io/)による[God Classの検出](https://docs.pmd-code.org/latest/pmd_rules_java_design.html#godclass)も試み，結果を比較せよ．
