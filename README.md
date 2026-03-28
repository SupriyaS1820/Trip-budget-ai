# 🌍 AI Trip Budget Planner

## 📌 Project Overview
This is an AI/ML-based web application that predicts travel expenses such as hotel cost, travel cost, and food cost based on user input.

---

## 🧠 Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn (Linear Regression)

---

## ⚙️ Features
- Predicts hotel, travel, and food expenses
- Suggests travel mode (Bus 🚌 / Flight ✈️)
- Calculates remaining budget
- User-friendly interface

---

## 📂 Project Structure
trip-budget-ai/
│
├── app.py
├── train_model.py
├── data.csv
├── model.pkl
├── requirements.txt
│
└── templates/
└── index.html

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Train the model
python train_model.py

3. Run the application
python app.py

4. Open in browser
http://127.0.0.1:5000

📊 Output

The application takes user input (destination, days, budget) and predicts:

Hotel cost
Travel cost
Food cost
Remaining budget
Suggested travel mode
🚀 Future Improvements
Add real-time travel APIs
Improve ML model accuracy
Add chatbot assistant
👩‍💻 Author

Supriya Suman

