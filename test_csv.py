#結合プログラム
import glob
import pandas as pd

#1---フォルダ内のCSVファイルの一覧を取得
files = sorted(glob.glob('./csv/report/*.csv'))
#2---ファイル数を取得
file_number = len(files)
#3---CSVファイルの中身を読み出して、リスト形式にまとめる
csv_list = []
for file in files:
    csv_list.append(pd.read_csv(file,encoding='utf-8',skiprows=[1],index_col=0))
#4---CSVファイルの結合
merge_csv = pd.concat(csv_list)
#5---CSVファイル出力
merge_csv.to_csv('./merge_nexpose.csv', encoding='utf-8')
#6---完了合図
print(file_number,' 個のCSVファイルを結合完了')