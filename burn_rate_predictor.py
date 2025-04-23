
import streamlit as st
import pandas as pd

# Load predictions CSV from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/ugocheee/burnoutpredictor2/main/predicted_burn_rate.csv"
    return pd.read_csv(url)

# Load the data
data = load_data()

# App Title
st.title("🔍 Employee Burn Rate Predictor")

# Employee ID selection
employee_id = st.selectbox("Select Employee ID:", sorted(data['Employee_ID'].unique()))

# Get prediction for selected ID
predicted_rate = data.loc[data['Employee_ID'] == employee_id, 'Predicted_Burn_Rate'].values[0]

# Display prediction
st.subheader(f"Predicted Burn Rate for Employee {employee_id}:")
st.metric(label="Burn Rate", value=f"{predicted_rate:.2f}")

# Optional chart
st.markdown("### 📊 Burn Rate Distribution")
st.bar_chart(data.set_index('Employee_ID')['Predicted_Burn_Rate'])
