import streamlit as st

def calculate_gross_salary(basic_salary):
    if basic_salary < 10000:
        hra = 0.67 * basic_salary
        da = 0.73 * basic_salary
    elif 10000 <= basic_salary <= 20000:
        hra = 0.69 * basic_salary
        da = 0.76 * basic_salary
    else:
        hra = 0.73 * basic_salary
        da = 0.89 * basic_salary

    gross_salary = hra + da + basic_salary
    return gross_salary

basic_salary = st.number_input("Enter your basic salary:", min_value=0.0, value=0.0, step=500.0)

if st.button('Calculate Gross Salary'):
    gross_salary = calculate_gross_salary(basic_salary)
    st.subheader(f"Your gross salary is: {gross_salary:.2f}")
