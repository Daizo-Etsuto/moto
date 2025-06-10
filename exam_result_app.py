# app.py
import streamlit as st

# 合否データ（受験番号, パスワード） → 結果
data = {
    ('3001', '1234'): '合格です。すごく良かったです。',
    ('3002', '1235'): '不合格です。',
    ('3003', '1236'): '合格です。',
    ('3004', '1237'): '不合格です。',
    ('3005', '1238'): '合格です。',
    ('3006', '1239'): '不合格です。',
    ('3007', '1240'): '合格です。',
    ('3008', '1241'): '不合格です。',
}

st.set_page_config(page_title="入塾テスト合否結果", page_icon="🔢")
st.title("📈 入塾テスト合否結果")
st.markdown("""
受験番号とパスワードを入力してください。
""")

# 入力欄
exam_id = st.text_input("受験番号")
password = st.text_input("パスワード", type="password")

# ボタン押下で確認
if st.button("確認する"):
    result = data.get((exam_id.strip(), password.strip()))
    if result:
        st.success(f"\u2705 【結果】{result}")
    else:
        st.error("⚠️ 受験番号あるいはパスワードが一致しません。")
