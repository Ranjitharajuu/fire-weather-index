import streamlit as st
import joblib
import numpy as np
from streamlit_folium import st_folium
import folium

# ---------------------------
# Load model + scaler
# ---------------------------
model = joblib.load("random_forest_fwi_model.pkl")
scaler = joblib.load("scaler_fwi.pkl")

st.set_page_config(page_title="FWI Prediction", layout="centered")

st.title("🔥 FWI Prediction")

st.write("Enter weather parameters and choose a location on the map.")

# ---------------------------
# INPUT FIELDS
# ---------------------------

col1, col2 = st.columns(2)

with col1:
    Temperature = st.number_input("Temperature", step=0.1)
    RH = st.number_input("Relative Humidity", step=0.1)
    Ws = st.number_input("Wind Speed", step=0.1)
    Rain = st.number_input("Rain", step=0.01, format="%.2f")
    FFMC = st.number_input("FFMC", step=0.1)

with col2:
    DMC = st.number_input("DMC", step=0.1)
    DC = st.number_input("DC", step=0.1)
    ISI = st.number_input("ISI", step=0.1)
    BUI = st.number_input("BUI", step=0.1)

st.subheader("📌 Select Location on Map")

# ---------------------------
# DEFAULT MAP (India Center)
# ---------------------------
default_lat = 20.5937
default_lon = 78.9629

m = folium.Map(location=[default_lat, default_lon], zoom_start=5)

# Allow click to choose location
m.add_child(folium.ClickForLatLng())

map_data = st_folium(m, height=350)

# Extract latitude & longitude
lat = None
lon = None

if map_data and "last_clicked" in map_data and map_data["last_clicked"]:
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]

st.write("### Selected Coordinates:")
st.write(f"Latitude: {lat}")
st.write(f"Longitude: {lon}")

# ---------------------------
# PREDICTION
# ---------------------------

if st.button("Predict FWI"):

    if lat is None or lon is None:
        st.error("⚠ Please select a location on the map.")
    else:
        # Prepare feature array
        features = np.array([[
            Temperature, RH, Ws, Rain,
            FFMC, DMC, DC, ISI, BUI
        ]], dtype=float)

        scaled = scaler.transform(features)
        pred = model.predict(scaled)[0]

        # Categorize risk
        if pred >= 25:
            level = "High"
            color = "red"
        elif pred >= 10:
            level = "Medium"
            color = "orange"
        else:
            level = "Low"
            color = "green"

        st.success(f"Predicted FWI: **{pred:.2f}**")
        st.markdown(f"### Fire Risk Level: <span style='color:{color};font-weight:bold'>{level}</span>", unsafe_allow_html=True)

        st.info(f"📍 Location: {lat:.6f}, {lon:.6f}")
