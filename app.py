import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="House Price AI", page_icon="🏠")
st.title("🏠 AI House Price Prediction")
st.write("أول مشروع AI ليكي - برافو!")

data = {
    'area': [50, 60, 70, 80, 90, 100, 110, 120],
    'rooms': [1, 2, 2, 3, 3, 3, 4, 4],
    'price': [500, 650, 700, 850, 900, 1000, 1100, 1250],
}
df = pd.DataFrame(data)
X = df[['area', 'rooms']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

st.sidebar.header("جربي الموديل")
area_input = st.sidebar.slider("المساحة", 30, 200, 80)
rooms_input = st.sidebar.slider("عدد الغرف", 1, 6, 3)

if st.sidebar.button("توقع السعر"):
    pred = model.predict([[area_input, rooms_input]])
    st.success(f"💰 السعر المتوقع: ${pred[0]:.0f}k")
    st.balloons()

st.dataframe(df)
