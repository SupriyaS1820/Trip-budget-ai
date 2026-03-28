import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Load dataset
data = pd.read_csv("data.csv")

# Step 2: Convert destination (text → number)
data['destination'] = data['destination'].astype('category').cat.codes

# Step 3: Features and labels
X = data[['destination', 'days', 'budget']]
y = data[['hotel_cost', 'travel_cost', 'food_cost']]

# Step 4: Train model
model = LinearRegression()
model.fit(X, y)

# Step 5: Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully and saved as model.pkl")