# Bengaluru_House_Price_Prediction_ML_Project  
This repository contains a **Machine Learning project** titled *Bengaluru House Price Prediction*.  
In this project, we build an interactive app that predicts house prices in Bengaluru based on user inputs such as **location, total square feet, number of bathrooms, and BHK size**.  
The prediction is powered by a trained ML model, ensuring accurate and reliable price estimates.  


##  Project Overview  
This project focuses on predicting **house prices in Bengaluru** using **Machine Learning techniques**.  
We developed an **interactive Streamlit web app** where users can input details like:  
-  Location  
-  Total Square Feet  
-  Number of Bathrooms  
-  Number of Bedrooms (BHK)  

Based on these inputs, the trained ML model predicts the **house price (in Lakhs)**.  


##  Dataset  
The dataset used in this project is the **Bengaluru House Price dataset**, which contains features such as:  
- Location  
- Total Square Feet  
- Number of Bathrooms  
- BHK (Bedrooms, Hall, Kitchen)  
- Price  

Preprocessing steps included:  
- Handling missing values  
- Feature engineering (converting location categories, standardizing inputs)  
- Outlier removal for better predictions  

---


##  Tech Stack  
- **Python**   
- **Pandas, NumPy** → Data processing  
- **Scikit-learn** → Model training & evaluation  
- **Joblib** → Saving trained model  
- **Streamlit** → Web app development  

---



##  How to Run the Project  

1. Clone the repository:  
   `
   git clone https://github.com/your-username/Bengaluru_House_Price_Prediction_ML_Project.git
   cd Bengaluru_House_Price_Prediction_ML_Project

2. Install dependencies:
    pip install -r requirements.txt

3. Run the Streamlit app:
    streamlit run app.py

4. Open the app in your browser → http://localhost:8501


## Results & Features

    - Clean UI for user-friendly predictions.

    - Accurate price estimation after data cleaning & feature engineering.

    - Error handling for unrealistic inputs (e.g., more bathrooms than bedrooms).

    - Reusable trained ML model.

Author:- Anshul Sharma