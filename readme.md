**Crime Rate Prediction Web App**
This project is a full-stack web application that predicts future crime rates in major Indian cities based on historical data (2019–2024).

🔍 Features
Select State, City, and Crime Type

Predict crime rates for 2025–2027 using Linear Regression

Displays safety status ("Safe" or "Unsafe") based on prediction

# 🛠 Tech Stack
Frontend:

HTML, JavaScript (Axios)

Backend:

Python (Flask)

scikit-learn for modeling

pandas for data manipulation

Flask-CORS for API access

📁 File Structure
crime_predictor/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend UI
├── data/
│ └── crime_data.csv # Dataset file
├── requirements.txt # Dependency list
├── README_Crime_Predictor.pdf

🚀 How to Run
Install dependencies:
pip install -r requirements.txt

Start the Flask server:
python app.py

Open browser at:
http://localhost:5000

📦 Dependencies
Flask

Flask-CORS

pandas

scikit-learn

✅ Dataset
The dataset contains 8 types of crimes across 5 cities in 8 Indian states from 2019 to 2024. It is used to train city-level crime prediction models.