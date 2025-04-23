import streamlit as st
import pandas as pd

# Load predictions CSV
@st.cache_data
def load_data():
    url = "https://github.com/ugocheee/burnoutpredictor2/blob/main/predicted_burn_rate.csv"
    return pd.read_csv(url)

data = load_data()

st.title("🔍 Employee Burn Rate Predictor")

# Dropdown to select Employee ID
employee_id = st.selectbox("Select Employee ID:", sorted(data['Employee_ID'].unique()))

# Fetch prediction
predicted_rate = data.loc[data['Employee_ID'] == employee_id, 'Predicted_Burn_Rate'].values[0]

# Display result
st.subheader(f"Predicted Burn Rate for Employee {employee_id}:")
st.metric(label="Burn Rate", value=f"{predicted_rate:.2f}")

# Optional visualization
st.markdown("### 📊 Burn Rate Distribution")
st.bar_chart(data.set_index('Employee_ID')['Predicted_Burn_Rate'])
