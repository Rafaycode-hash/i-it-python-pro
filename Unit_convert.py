import streamlit as st

# Heading
st.title("Simple Unit Converter")

# Units available
units = {
    "Kilometer": 1000,
    "Meter": 1,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254
}

# Input from user
value = st.number_input("Enter value to convert:", value=0.0)
from_unit = st.selectbox("From Unit:", list(units.keys()))
to_unit = st.selectbox("To Unit:", list(units.keys()))

# Conversion
if st.button("Convert"):
    # Step 1: Convert from "from_unit" to meters
    value_in_meters = value * units[from_unit]
    # Step 2: Convert meters to "to_unit"
    result = value_in_meters / units[to_unit]
    st.success(f"{value} {from_unit} = {result} {to_unit}")
