# 🚖 Uber Rides Prediction Using Machine Learning

This project predicts the **number of weekly Uber rides** in a city based on factors like price per week, population, monthly income, and parking availability.  
It uses a **Linear Regression model** trained on historical Uber data, with a **Flask web app** frontend.

---

## 📌 Features
- Machine Learning model (Scikit-Learn Linear Regression)
- Flask-based web interface
- User input form for prediction
- Clean UI with HTML, CSS
- Model trained on real-world dataset (`uber_dataset.csv`)

---

## 📂 Project Structure
Uber-Rides-Prediction/
│
├── app.py # Flask application
├── Model_Training.py # Model training script
├── model.pkl # Trained ML model (pickle file)
├── uber_dataset.csv # Dataset used for training
│
├── templates/
│ └── index.html # Frontend HTML
│
├── static/
│ └── css/
│ ├── style.css # Styling for web app
│ └── Uber.jpg # Background image
│
└── README.md # Project documentation

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Uber-Rides-Prediction.git
cd Uber-Rides-Prediction
```
### 2. Create a virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Train the model
python Model_Training.py

### 5. Run the Flask app
python app.py

Go to 👉 http://127.0.0.1:5000/ in your browser.
