import streamlit as st

def calculate_total_score(project, internal, external):
    if project < 50:
        st.error(f"You failed the project with score: {project}")
    if internal < 50:
        st.error(f"You failed the internal score with score: {internal}")
    if external < 50:
        st.error(f"You failed the external score with score: {external}")

    if project >= 50 and internal >= 50 and external >= 50:
        total_score = (project * 0.7) + (internal * 0.1) + (external * 0.2)

        if total_score >= 90:
            grade = "A"
        elif total_score >= 80:
            grade = "B"
        else:
            grade = "C"

        st.subheader(f"Total score: {total_score:.2f}%")
        st.subheader(f"Grade: {grade}")

project = st.number_input("Enter project score (out of 100):", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
internal = st.number_input("Enter internal score (out of 100):", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
external = st.number_input("Enter external score (out of 100):", min_value=0.0, max_value=100.0, value=0.0, step=1.0)

if st.button("Calculate Grade"):
    calculate_total_score(project, internal, external)
