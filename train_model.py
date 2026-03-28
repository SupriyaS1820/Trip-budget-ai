import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("data.csv")
data['destination'] = data['destination'].astype('category').cat.codes
X = data[['destination', 'days', 'budget']]
y = data[['hotel_cost', 'travel_cost', 'food_cost']]
model = LinearRegression()
model.fit(X, y)
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully and saved as model.pkl")