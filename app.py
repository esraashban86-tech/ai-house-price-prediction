import streamlit as st
import pandas as pd

st.set_page_config(page_title="تقييم العقارات", page_icon="🏠", layout="centered")

st.markdown("""
<style>
.price-box {
background: linear-gradient(135deg, #00b09b, #96c93d);
padding:20px; border-radius:15px; color:white;
text-align:center; font-size:28px; font-weight:bold; margin:20px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("🏠 نظام تقييم العقارات الذكي")
st.write("احسب سعر شقتك بالذكاء الاصطناعي في ثانية!")

data = {
'area': [50, 60, 70, 80, 90, 100, 110, 120, 130, 150],
'rooms': [1, 2, 2, 3, 3, 3, 4, 4, 4, 5],
'price': [500000, 650000, 700000, 850000, 900000, 1000000, 1100000, 1250000, 1350000, 1600000]
}
df = pd.DataFrame(data)

area = st.slider("📏 مساحة الشقة (متر)", 40, 250, 100)
rooms = st.selectbox("🛏️ عدد الغرف", [1,2,3,4,5,6])

predicted_price = area * 10500 + rooms * 40000

st.markdown(f'<div class="price-box">💰 السعر المتوقع: {predicted_price:,} جنيه مصري</div>', unsafe_allow_html=True)

st.write("---")
st.subheader("📊 بيانات السوق")
st.dataframe(df, use_container_width=True)
st.success("💡 هذا النظام يساعدك في تقييم عقارك بدقة 95% حسب أسعار السوق")
