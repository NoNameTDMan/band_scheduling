import streamlit as st

VERSION = "1.4.0" #as of 2025-12-01

st.set_page_config(page_title="固定枠作成ツール", page_icon=":shark:")

with open("changelog.md", "r", encoding="utf-8") as f:
    changelog_content = f.read()

st.title("トップページ（仮）")
st.markdown(f"<p style='text-align: right; color: gray;'>ver. {VERSION}</b></p>", unsafe_allow_html=True)

with st.expander("バージョン履歴", expanded=False):
    st.caption(changelog_content)

