# SI = PNR/100

principal = 10000
years = 2
interest = 8

result = principal * years * interest / 100

print(result)

#===================================================

import streamlit as st

st.title("Simple Interest Calculator")

st.subheader("Enter the principal amount")
principal = st.number_input("Principal")

st.header("Enter the number of years")
# years = st.number_input("Years")
years = st.slider("Years", min_value=1, max_value=10, value=2)

st.header("Enter the rate of interest")
interest = st.number_input("Interest")

st.button("Calculate")

if st.button:
    result = principal * years * interest / 100
    st.header("The simple interest is")
    st.success(result)


