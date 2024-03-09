import streamlit as st

#ヘッダー表示
st.header("streamlitテストアプリ")
#タイトル表示
st.title("Webアプリ開発中")
#テキスト表示
st.write("生活用アプリ")

#スライダー（デフォルトでは0~100）
st.title("スライダー")
weight = st.slider("今日の体重は")
st.write("今の体重は" + str(weight) +"kgです")

#ボタン
st.title("今日の天気は")
st.button("リセット", type="primary")
if st.button("晴れ？"):
    st.write("今日も元気に！")
else:
    st.write("傘を忘れずに")

#テキスト入力
st.title("やること")
st.text_input("今やること", key="do")
st.session_state.do #keyでアクセス

#チェックボックス
st.title("ごみ捨てチェック")
is_agree = st.checkbox("ごみ捨てた？")
if is_agree:
    st.write("お疲れ様！")
else:
    st.write("忘れずに！")


import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 100, (20,5)), columns=("国語", "数学", "理科", "社会", "英語"))

#表の表示
##サイドバーを活用
st.sidebar.title("テストの結果")
st.sidebar.dataframe(df) 

#棒グラフ
st.title("国語の成績")
st.bar_chart(df["国語"])

#折れ線グラフ
st.title("数学")
st.line_chart(df["数学"])

#散布図
df["合計"]=df["国語"]+df["数学"]+df["英語"]+df["理科"]+df["社会"]
st.title("理科と数学の関係")
st.scatter_chart(df, x = "理科", y = "数学", size="合計")

#Mapに散布図を表示
st.title("東京駅付近に散布図")
mapdf = pd.DataFrame(
    # 東京駅付近
    np.random.rand(50, 2)/[50, 50]  + [35.68, 139.76],
    # latitude 緯度 longitude 経度
    columns=['lat', 'lon']
)

st.map(mapdf)