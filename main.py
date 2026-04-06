import streamlit as st

st.set_page_config(page_title="固定枠作成ツール", page_icon=":material/music_note:")

top_page = st.Page(page="contents/top_page.py", title="How to Use", icon=":material/info:")
make_csv = st.Page(page="contents/make_csv.py", title="CSVファイル作成ツール", icon=":material/csv:")
scheduling = st.Page(page="contents/band_practice_schedule.py", title="固定枠作成ツール", icon=":material/handyman:")
pg = st.navigation([top_page, make_csv, scheduling])
pg.run()

