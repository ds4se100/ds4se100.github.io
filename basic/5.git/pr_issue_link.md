[【トップページへ戻る】](../../)

# **基本編5：PR・Issue連携分析**

## 51 [PR] PRのリードタイムを計算せよ

## 52 [PR] GitHubAPIでcreated_atとmerged_atを取得し、時間を計測

## 53 [PR] PRに紐づくコミットを特定せよ

    GitHub APIで、PRに含まれるSHAリストを取得
    
    PyGithub等で、PRに紐づくコミットを特定
    
   （注意）squash mergeだと履歴上1コミットしか残らないためGit logでは履歴を追えない。GitHub APIなら可能
   
## 54 [PR] mergeされたPRとmergeされずにcloseされたPRの特徴を比較せよ

    GitHub APIで、修正回数、レビューコメント数、変更行数、ファイル数、レビュー数、提出者の経験、リードタイムなどを比較
    
## 55 [IssueとPR] PRと紐づくIssueを特定せよ

   （方法1）PRの本文・タイトルから Issue番号を特定
   
   （方法2）IssueのGitHubの Closing keywords からIssue番号を特定
   
   （方法3）コミットメッセージからIssue番号を特定
   
   （方法4）時間・開発者ベースの推定 - heulistic linking -
   
## 56 [IssueとPR] Issueとコミットのリンク率を算出せよ

## 57 [IssueとPR] Issueクローズとコミットの時間差を分析せよ

## 58 Issueのclose時刻、PRが含まれるコミットとその時刻を特定し、計算

## 59 コントリビュータとメンテナ（merge権限あり）の役割を分析せよ
    PR提出数、PR提出数、PRマージ率、レビューコメント数、変更行数、PRリードタイムなどを調査

## 60 PR中心開発と直接コミット開発を比較せよ
