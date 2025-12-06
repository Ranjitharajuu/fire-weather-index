🔥 Fire Weather Index (FWI) Prediction – Streamlit Application

This project is a Machine Learning–powered Fire Weather Index (FWI) prediction system built using a Random Forest model and deployed through Streamlit.
The app predicts FWI from weather parameters and also provides a map-based visualization, helping understand geographic fire-risk distribution.

🌟 Features
✔️ Streamlit Interactive UI

A user-friendly interface that accepts inputs such as temperature, humidity, wind speed, rainfall, etc., and instantly provides predictions.

✔️ Machine Learning Prediction

Uses a trained Random Forest model

Includes a StandardScaler for preprocessing

Outputs a numeric FWI score representing fire danger level

✔️ 🗺️ Map Visualization (Geospatial Component)

The app includes a map section where predicted FWI values can be displayed based on location inputs.
This visual map allows users to:

View how fire danger varies across regions

Understand geographic hotspots

Interactively explore FWI intensity on a real map

Enhance decision-making for forest safety and resource planning

The map may use:

Streamlit’s built-in st.map()

Latitude–longitude inputs

Geospatial plotting (e.g., scatter points representing fire risk)

✔️ Dataset Included

The dataset used for training/testing the model is also provided (Fwi dataset.csv).

✔️ Easy Deployment

The requirements.txt file makes the entire project easy to install and run anywhere.

📂 Project Structure
fire-weather-index/
│── app.py                 # Streamlit app with map + prediction UI
│── random_forest_fwi_model.pkl
│── scaler_fwi.pkl
│── Fwi dataset.csv
│── requirements.txt
│── README.md
│── .gitignore

🚀 How to Run the App Locally
1️⃣ Install all dependencies
pip install -r requirements.txt

2️⃣ Start the Streamlit app
streamlit run app.py


The app will open at:
👉 http://localhost:8501/

🗺️ Map Feature — Detailed Explanation

The application includes a geographical map visualization that helps users understand fire-risk severity across different coordinates.

This part of the app can:

Display user-selected locations using latitude & longitude

Plot predicted FWI values as points on the map

Highlight high-risk areas visually

Provide an intuitive representation instead of just numeric values

This feature enhances usability by combining ML prediction + spatial insight, making the tool more practical for forest officers, emergency teams, and researchers.

🧠 Model Information
Algorithm:

Random Forest Regressor

Inputs:

Temperature

Relative Humidity

Wind Speed

Rainfall

Other meteorological factors

Output:

FWI Score
Higher scores → higher fire risk.
