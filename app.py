import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("house_price_model.pkl")

# Load locations list
locations = joblib.load("locations.pkl")


st.title("Bengaluru House Price Prediction App")

# Dropdown inputs
location = st.selectbox("Select Location", locations)

# You can adjust options as per your dataset ranges
sqft = st.selectbox("Total Sqft", [500, 750, 1000, 1200, 1500, 1800, 2000, 2500, 3000, 4000, 5000])
bath = st.selectbox("Number of Bathrooms", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bhk = st.selectbox("Number of Bedrooms (BHK)", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if st.button("Predict Price"):
    if bhk < bath:
        st.error("⚠️ A house cannot have more bathrooms than bedrooms. Please adjust your inputs.")
    elif sqft < 300:
        st.error("⚠️ Minimum house size should be at least 300 sqft.")
    else:
        data = pd.DataFrame([{
            "location": location,
            "total_sqft": sqft,
            "bath": bath,
            "BHK": bhk
        }])
        prediction = model.predict(data)[0]
        st.success(f"💰 Predicted Price: {prediction:.2f} Lakhs")

