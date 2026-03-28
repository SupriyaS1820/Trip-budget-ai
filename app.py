from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Destination mapping (IMPORTANT)
dest_map = {
    "Manali": 0,
    "Goa": 1,
    "Jaipur": 2,
    "Delhi": 3,
    "Mumbai": 4,
    "Shimla": 5,
    "Udaipur": 6,
    "Agra": 7,
    "Varanasi": 8,
    "Kerala": 9,
    "Darjeeling": 10,
    "Rishikesh": 11,
    "Ladakh": 12,
    "Ooty": 13,
    "Andaman": 14
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    destination = request.form['destination']
    days = int(request.form['days'])
    budget = int(request.form['budget'])

    dest_code = dest_map.get(destination, 0)

    prediction = model.predict([[dest_code, days, budget]])

    hotel, travel, food = prediction[0]

    remaining = budget - (hotel + travel + food)

    travel_mode = "Bus 🚌" if travel < 3000 else "Flight ✈️"

    return render_template("index.html",
                           hotel=round(hotel),
                           travel=round(travel),
                           food=round(food),
                           remaining=round(remaining),
                           mode=travel_mode)

if __name__ == "__main__":
    app.run(debug=True)
    import webbrowser

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)