import streamlit as st

salary = st.number_input("Enter your salary:", min_value=0.0, value=0.0, step=100.0)
bill1 = st.number_input("Enter the first shopping bill amount:", min_value=0.0, value=0.0, step=10.0)
bill2 = st.number_input("Enter the second shopping bill amount:", min_value=0.0, value=0.0, step=10.0)
bill3 = st.number_input("Enter the third shopping bill amount:", min_value=0.0, value=0.0, step=10.0)

total_shopping_expense = bill1 + bill2 + bill3
st.subheader(f"Total shopping expense: {total_shopping_expense}")

if total_shopping_expense > salary:
    st.success("You are spending more than your salary on shopping!")
else:
    remaining_balance = salary - total_shopping_expense
    st.error(f"You have {remaining_balance} left after shopping.")
