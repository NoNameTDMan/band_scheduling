import streamlit as st
import csv
from datetime import datetime, timedelta
import pandas as pd

st.title("CSVファイル作成ツール")

# session_state のキーはウィジェット作成前に初期化しておく
if "band_name_input" not in st.session_state:
    st.session_state["band_name_input"] = ""

band_name = st.text_input("バンド名を入力してください", key="band_name_input")
initial_date = datetime(2025, 1, 1)

st.session_state.dates = [datetime(2025, 1, 1), datetime(2025, 1, 1)]
st.session_state.dates = st.date_input("期間を選択してください", st.session_state.dates)

period_list = [1, 2, 3, 4, 5, 6]

if band_name != "" and len(st.session_state.dates) == 2:
    
    start_date = st.session_state.dates[0]
    end_date = st.session_state.dates[1]
    
    
    st.write("バンド名：", band_name)
    st.write("練習期間：", f"{start_date} 〜 {end_date}")
    
    date_list = [start_date + timedelta(days=i)
                 for i in range((end_date - start_date).days + 1)]
    date_list_int = [int((start_date + timedelta(days=i)).strftime("%m%d"))
                 for i in range((end_date - start_date).days + 1)]

    input_dict = {}
    df = pd.DataFrame("", index=period_list, columns=date_list)
    df[:] = None
    
    for i, date in enumerate(date_list):
        input_dict[date] = st.multiselect(f"日付：{date}", options=period_list, default=[], key=f"date_{date}")
        input_dict[date].sort()
        for period in input_dict[date]:
            df.at[period, date] = 1
        
    st.write("ファイル名：", f"{band_name}.csv")
    st.dataframe(df)
    
    if st.button("CSVファイルを作成"):
        for date in date_list:
            for period in period_list:
                if df.at[period, date] != 1:
                    df.at[period, date] = 0
        
        csv_filename = f"{band_name}.csv"
        df_to_save = df.copy()
        df_to_save.columns = date_list_int
        df_to_save = df_to_save.fillna(0).astype(int)
        df_to_save.to_csv(csv_filename, header=False, index=False)
        st.success(f"CSVファイル '{csv_filename}' を作成しました。")
        with open(csv_filename, "rb") as f:
            st.download_button(
                label="CSVファイルをダウンロード",
                data=f,
                file_name=csv_filename,
                mime="text/csv"
            )
    
    def _reset():
        # ウィジェットキーの変更はコールバック内で行う（ウィジェット作成の前/後でも安全）
        st.session_state["band_name_input"] = ""
        for date in date_list:
            key = f"date_{date}"
            if key in st.session_state:
                del st.session_state[key]
        # コールバックが完了すると Streamlit は自動的に再実行されるため
        # 明示的な再実行呼び出しは不要（または古いバージョンで未定義の可能性がある）
        return

    st.button("リセット", on_click=_reset)
    