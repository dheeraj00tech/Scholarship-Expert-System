"""Streamlit UI. Run with:  streamlit run app.py"""
import streamlit as st
from engine import evaluate_all

st.set_page_config(page_title="Smart Scholarship Eligibility System", page_icon="🎓")
st.title("🎓 Smart Scholarship Eligibility System")
st.caption("A rule-based expert system: enter your details and see which scholarships you qualify for, and why.")

with st.form("student_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Student name (optional)")
        category = st.selectbox("Category", ["General", "EWS", "OBC", "SC", "ST"])
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        state = st.selectbox("Home state", ["Himachal Pradesh", "Punjab", "Haryana", "Delhi", "Other"])
    with col2:
        income = st.number_input("Annual family income (Rs)", min_value=0, value=300000, step=10000)
        cgpa = st.number_input("CGPA (out of 10)", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
        level = st.selectbox("Level of study", ["Undergraduate", "Postgraduate", "Diploma"])
        course = st.selectbox("Course", ["B.Tech / Engineering", "Science", "Commerce", "Arts", "Other"])
    disability = st.checkbox("I have a disability (40% or more)")
    submitted = st.form_submit_button("Check eligibility")

if submitted:
    facts = {
        "category": category, "gender": gender, "state": state,
        "income": income, "cgpa": cgpa, "level": level,
        "course": course, "disability": disability,
    }
    eligible, not_eligible = evaluate_all(facts)

    st.subheader(f"Results{' for ' + name if name else ''}")
    st.metric("Eligible scholarships", len(eligible))

    if eligible:
        for r in eligible:
            with st.expander(f"✅ {r['name']}  (priority {r['priority']})", expanded=True):
                st.write(f"**Provider:** {r['provider']}")
                st.write(f"**Benefit:** {r['benefit']}")
                st.write("**Why you qualify:**")
                for p in r["passed"]:
                    st.write(f"- ✔ {p}")
    else:
        st.warning("No scholarships matched. See the near-misses below.")

    st.subheader("Not eligible (and why)")
    for r in not_eligible:
        with st.expander(f"❌ {r['name']}  ({r['match_percent']}% of conditions met)"):
            for p in r["passed"]:
                st.write(f"- ✔ {p}")
            for f_ in r["failed"]:
                st.write(f"- ✘ Not met: {f_}")

    st.info("Sample criteria for demonstration only. Always confirm current rules on the official scholarship portal.")
