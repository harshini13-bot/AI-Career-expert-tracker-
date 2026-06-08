import streamlit as st
from inference import forward_chaining

st.set_page_config(
    page_title="AI Career Guidance Expert System",
    page_icon="🎓"
)

st.title("🎓 AI Career Guidance Expert System")

st.write(
    "Select your interests and skills."
)

options = [

    "programming",
    "maths",
    "python",
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

    results, steps = forward_chaining(selected)

    st.subheader("Reasoning Path")

    if steps:

        for step in steps:
            st.info(step)

    else:
        st.warning(
            "No rule fired."
        )

    st.subheader("Recommended Careers")

    recommendations = []

    for item in results:

        if item not in selected:

            recommendations.append(item)

    if recommendations:

        for r in recommendations:
            st.success(r.replace("_", " ").title())

    else:
        st.error(
            "No recommendation found."
        )