import streamlit as st
from inference import recommend_careers

st.set_page_config(
    page_title="AI Career Guidance Expert System",
    page_icon="🎓"
)

st.title("🎓 AI Career Guidance Expert System")


st.write(
    "Select your skills and interests to discover suitable career paths."
)

options = [

    "programming",
    "python",
    "maths",
    "web_development",
    "design",
    "creativity",
    "data_analysis",
    "statistics",
    "cybersecurity",
    "networking",
    "ethical_hacking",
    "cloud",
    "linux"

]

selected = st.multiselect(
    "Choose Skills/Interests",
    options
)

if st.button("Get Career Recommendation"):

    recommendations, reasoning = recommend_careers(
        selected
    )

    st.subheader("Reasoning Path")

    for step in reasoning:
        st.info(step)

    st.subheader("Top Career Recommendations")

    if recommendations:

        for career in recommendations[:5]:

            st.success(
                f"{career['career']} ({career['score']}% Match)"
            )

            st.write(
                f"Description: {career['description']}"
            )

            st.write(
                f"Average Salary: {career['salary']}"
            )

            st.divider()

    else:

        st.warning(
            "Please select more skills."
        )