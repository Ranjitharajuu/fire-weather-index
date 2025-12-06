# 🔥 Fire Weather Index (FWI) Prediction – Streamlit Application

This project is a **Machine Learning-based Fire Weather Index (FWI) prediction system** built using a **Random Forest model** and deployed with **Streamlit**.  
It predicts the likelihood of fire danger based on weather parameters such as temperature, humidity, wind speed, etc.

---

## 🌟 Features

### ✔️ Streamlit User Interface  
An interactive UI where users enter weather inputs and instantly receive an FWI prediction.

### ✔️ Machine Learning Model  
- Trained Random Forest model (`random_forest_fwi_model.pkl`)
- Scaler for input normalization (`scaler_fwi.pkl`)

### ✔️ Preprocessed Dataset  
Dataset used for training/testing the FWI model.

### ✔️ Easy Deployment  
Uses `requirements.txt` for installing dependencies.

---

## 📂 Project Structure

```
fire-weather-index/
│── app.py
│── random_forest_fwi_model.pkl
│── scaler_fwi.pkl
│── Fwi dataset.csv
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🚀 How to Run the App Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit app
```bash
streamlit run app.py
```
---

## 🧠 Model Details
- Algorithm: **Random Forest Regressor**
- Input Features:
  - Temperature
  - Relative Humidity
  - Wind Speed
  - Rain
  - Other weather-related attributes
- Output: **Fire Weather Index (FWI)** score

---



