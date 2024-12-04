
import streamlit as st

def calculate_recalculation(actual_temp, norm_temp, tariff_rate, norm_consumption, actual_consumption):
    # Ensure inputs are valid
    if actual_temp is None or norm_temp is None or tariff_rate is None or norm_consumption is None or actual_consumption is None:
        return "Please provide all inputs."
    if tariff_rate <= 0 or norm_consumption <= 0 or actual_consumption <= 0:
        return "Inputs must be positive numbers."
    
    # Calculate recalculation
    try:
        adjustment = (actual_consumption - norm_consumption) * tariff_rate
        return adjustment
    except Exception as e:
        return f"Error in calculation: {e}"

st.title("Heating Cost Recalculation")

# Input fields
system_type = st.selectbox("System Type (Open/Closed)", ["Open", "Closed"])
actual_temp = st.number_input("Actual Outdoor Temperature (°C)", value=-10.0)
norm_temp = st.number_input("Normative Outdoor Temperature (°C)", value=-15.0)
tariff_rate = st.number_input("Tariff Rate for Heating (Tenge/Gcal)", value=4000.0)
norm_consumption = st.number_input("Norm Consumption (Gcal/m²)", value=0.02)
actual_consumption = st.number_input("Actual Consumption (Gcal/m²)", value=0.018)

# Calculate button
if st.button("Calculate Recalculation"):
    result = calculate_recalculation(actual_temp, norm_temp, tariff_rate, norm_consumption, actual_consumption)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"Recalculation Result: {result:.2f} Tenge per m²")
