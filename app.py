import streamlit as st

import pandas as pd

import plotly.express as px

# 網頁設定

st.set_page_config(

    page_title="AutoMoney 智慧記帳系統",

    page_icon="💰",

    layout="wide"

)

# 深色主題 CSS

st.markdown("""

<style>

body {

    background-color: #0E1117;

    color: white;

}

.main {

    background-color: #0E1117;

}

h1, h2, h3, h4 {

    color: white;

}

.block-container {

    padding-top: 2rem;

}

.card {

    background-color: #1B1F2A;

    padding: 20px;

    border-radius: 15px;

    margin-bottom: 20px;

}

.feature-icon {

    font-size: 40px;

}

</style>

""", unsafe_allow_html=True)

# 側邊欄

st.sidebar.title("📌 AutoMoney")

page = st.sidebar.radio(

    "選擇頁面",

    ["首頁", "功能展示", "數據分析", "商業模式"]

)

# 首頁

if page == "首頁":

    st.title("💰 AutoMoney 智慧記帳系統")

    st.subheader("全自動化 AI 財務追蹤平台")

    st.markdown("""

    <div class="card">

    現代人每天使用 LINE Pay、Apple Pay、信用卡與電子支付，

    導致記帳資訊分散且難以管理。

    我們的系統結合：

    - OCR 發票辨識

    - AI 自動分類

    - 消費分析 Dashboard

    - 雲端同步

    讓記帳從「手動輸入」變成「自動完成」。

    </div>

    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""

        <div class="card">

        <div class="feature-icon">📷</div>

        <h3>OCR 辨識</h3>

        拍照即可自動辨識收據與發票。

        </div>

        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""

        <div class="card">

        <div class="feature-icon">🤖</div>

        <h3>AI 分類</h3>

        自動分類交通、餐飲與生活支出。

        </div>

        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""

        <div class="card">

        <div class="feature-icon">📊</div>

        <h3>數據分析</h3>

        自動生成每月支出圖表。

        </div>

        """, unsafe_allow_html=True)

# 功能展示

elif page == "功能展示":

    st.title("🚀 功能展示")

    uploaded_file = st.file_uploader(

        "📷 上傳收據圖片",

        type=["png", "jpg", "jpeg"]

    )

    if uploaded_file:

        st.image(uploaded_file, width=300)

        st.success("✅ OCR 辨識成功！")

        st.write("### 辨識結果")

        st.write("商店：7-ELEVEN")

        st.write("金額：NT$120")

        st.write("分類：餐飲")

    st.divider()

    st.subheader("📩 自動同步支付紀錄")

    st.info("""

    系統可自動同步：

    - Apple Pay

    - LINE Pay

    - 信用卡通知

    - 電子發票

    """)

# 數據分析

elif page == "數據分析":

    st.title("📊 財務分析 Dashboard")

    data = pd.DataFrame({

        "類別": ["餐飲", "交通", "娛樂", "購物", "生活"],

        "金額": [3500, 1200, 1800, 2500, 1500]

    })

    fig = px.pie(

        data,

        names="類別",

        values="金額",

        title="每月支出比例"

    )

    st.plotly_chart(fig, use_container_width=True)

    bar = px.bar(

        data,

        x="類別",

        y="金額",

        title="支出分析"

    )

    st.plotly_chart(bar, use_container_width=True)

# 商業模式

elif page == "商業模式":

    st.title("💼 商業模式")

    st.markdown("""

    <div class="card">

    <h3>🎯 目標客群</h3>

    • 數位支付使用者  

    • 預算管理學生  

    • 自由工作者  

    • 財務規劃族群  

    </div>

    """, unsafe_allow_html=True)

    st.markdown("""

    <div class="card">

    <h3>💳 訂閱方案</h3>

    ✅ 基礎版：免費  

    ✅ 月費版：NT$49  

    ✅ 年費版：NT$499  

    </div>

    """, unsafe_allow_html=True)

    st.markdown("""

    <div class="card">

    <h3>⚠️ 專案特色</h3>

    • Open Source 開源  

    • Local First 本地執行  

    • 高隱私安全性  

    • AI 自動化記帳  

    </div>

    """, unsafe_allow_html=True)
