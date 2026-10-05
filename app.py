# AI House Price Prediction - My First AI Project
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Create simple dataset
data = {
    'area': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'rooms': [1, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    'price': [500, 650, 700, 850, 900, 1000, 1150, 1200, 1300, 1450]
}
df = pd.DataFrame(data)

# 2. Train AI model
X = df[['area', 'rooms']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# 3. Test the model
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# 4. Predict new house
new_house = [[100, 3]] # 100m, 3 rooms
predicted_price = model.predict(new_house)
print(f"Predicted price for 100m, 3 rooms: {predicted_price[0]:.0f}k EGP")
