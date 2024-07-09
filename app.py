import pandas as pd
import time
from flask import Flask, render_template

app = Flask(__name__)

url = './xlsx/sample.csv'

def load_csv_data():
    start = time.time()
    # 列指定usecols
    # データタイプ文字列指定 dtype=str
    df = pd.read_csv(url, header=0, usecols=[0, 3, 7, 8], dtype=str, na_values='-')
    end = time.time()
    print("CSVの読み込み時間:", end - start)
    print(df)
    return df

@app.route('/', methods=("POST", "GET"))
def index():
    df_data = load_csv_data()
    data_list = df_data.to_dict(orient='records')
    return render_template('index.html', data_list=data_list)

if __name__ == '__main__':
    app.run(debug=True)
