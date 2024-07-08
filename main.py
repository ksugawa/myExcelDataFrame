import pandas as pd
import numpy as np
import time

url = './xlsx/sample.csv'

start = time.time()
# 列指定usecols
# データタイプ文字列指定 dtype=str
# 列指定のデータタイプ文字列指定 dtype={0: float, 3: str}

df = pd.read_csv(url, header=0, usecols=[0,3,7,8], dtype=str, na_values='-') 

end = time.time()
print("CSVの読み込み時間:", end - start)
print(df.isnull())
