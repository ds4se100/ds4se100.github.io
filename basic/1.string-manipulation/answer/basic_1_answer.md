## 11. 文字列の置換
ある学生の学籍番号EN26CS0337からen26cs0337@softwareknock.eduというメールアドレスを作成したい．
学籍番号の大文字を小文字に置換する，すなわちEN26CS0337をen26cs0337に変換して出力しなさい．


```python
sid = "EN26CS0337"
lower_sid = sid.lower()
print("13:", lower_sid)  # en26cs0337
```

## 12. 文字列の結合
en26cs0337の後ろに@softwareknock.eduを追加し，メールアドレスen26cs0337@softwareknock.eduを作成して出力しなさい


```python
local = "en26cs0337"
email = local + "@softwareknock.edu"
print(email)
```

## 13. 文字列の抽出 1
EN17CS0337から数字だけを抽出した170337という文字列をisdigit()を使って作成・出力しなさい．


```python
sid = "EN17CS0337"

sid_digits = ""
for ch in sid:
    if ch.isdigit():
        sid_digits += ch

print(sid_digits)  # 170337
```

## 14. 文字列の抽出 2
13をis.digit()を使わずに，すなわちEN17CS0337から数字である3-4文字目，7-10文字目を抽出・結合し，170337という文字列を作成・出力しなさい．


```python
sid = "EN17CS0337"

digit_part1 = sid[2:4]   # 3〜4文字目（インデックス2,3）
digit_part2 = sid[6:10]  # 7〜10文字目（インデックス6,7,8,9）

sid_digit = digit_part1 + digit_part2
print(sid_digit)  # 170337
```

## 15. 文字列の抽出 3
13, 14の処理を正規表現を用いて行いなさい


```python
import re

sid = "EN17CS0337"

# 数字だけ抽出
digits = "".join(re.findall(r"\d", sid))
print(digits)  # 170337
```

## 16. チェックディジット（数値）の付加
170337の「末尾に」1桁の数字を加えて，9で割り切れるようにしなさい


```python
sid_digit = 170337

# 末尾に付ける 0-9 を探す
add = 0
for x in range(10):
    if (sid_digit * 10 + x) % 9 == 0:
        add = x
        break

result = sid_digit*10 + add
print(result)        # 1703376
```

## 17. チェックディジット（数値）の検査
1703376が9で割り切れるか確認し，確認できれば「9で割り切れる」，できなければ「9で割り切れない」と回答しなさい


```python
sid_digit = 1703376

if sid_digit % 9 == 0:
    print("9で割り切れる")
else:
    print("9で割り切れない")

```

## 18. チェックディジット（文字）の付加
170337の「末尾に」1文字のアルファベットを加えて，11で割り切れるようにしなさい．数字とアルファベットの対応表は以下の通りである．

|A|B|C|H|K|M|R|U|X|Y|Z|
|----|----|----|----|----|----|----|----|----|----|----|
|0|1|2|3|4|5|6|7|8|9|10|



```python
sid = 170337

val_to_alpha = {
    0: "A", 1: "B", 2: "C", 3: "H", 4: "K", 5: "M",
    6: "R", 7: "U", 8: "X", 9: "Y", 10: "Z"
}

chosen_x = 0
for x in range(11):
    if (sid * 10 + x) % 11 == 0:
        chosen_x = x
        break
# 変換表を用いて末尾の数値をアルファベットに変換して結合
result = str(sid) + val_to_alpha[chosen_x]
print(result)  # 170337C
```

## 19. チェックディジット（文字）の検査
170337Cが11で割り切れるか確認し，確認できれば「11で割り切れる」，できなければ「11で割り切れない」と回答しなさい．アルファベットと数字の対応表は20と同様とする．


```python
sid = "170337C"

alpha_to_val = {
    "A": 0, "B": 1, "C": 2, "H": 3, "K": 4, "M": 5,
    "R": 6, "U": 7, "X": 8, "Y": 9, "Z": 10
}

# 数値とチェックディジットに分離
sid_main = sid[:-1]
sid_cd = sid[-1]

# チェックディジットを数値に変換
num_cd = alpha_to_val[sid_cd]
sid_full = int(sid_main) * 10 + num_cd

if sid_full % 11 == 0:
    print("11で割り切れる")
else:
    print("11で割り切れない")
print(n)
```
