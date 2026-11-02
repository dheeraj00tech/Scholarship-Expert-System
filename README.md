

<img width="1037" height="782" alt="Screenshot 2026-11-02 at 9 01 16 PM" src="https://github.com/user-attachments/assets/6f76cb72-5695-48e7-92d4-c7f81ec4074d" />









# 🎓 Smart Scholarship Eligibility System

A rule-based **expert system** that tells a student which scholarships they are eligible for, and **explains why** (or why not).

Built as an AI project for **Unit VI: Expert Systems**.

## 🔗 Live Demo

**Try it here (no installation needed):**
https://scholarship-expert-system-esuysfzw68gwokfrnexnh2.streamlit.app/

## 💡 What does it do?

1. The student fills in a simple form (category, income, CGPA, gender, state, course, etc.).
2. The system checks the details against the rules of every scholarship.
3. It shows:
   - ✅ **Eligible scholarships**, with the reasons the student qualifies
   - ❌ **Not eligible scholarships**, with the exact conditions that were not met
   - Eligible scholarships are sorted by priority

## 🧠 How it works (Expert System Components)

| Expert System Part | Where it is in this project | What it does |
|---|---|---|
| **Knowledge Base** | `scholarships.json` | Stores all scholarships and their IF-THEN rules |
| **Inference Engine** | `engine.py` | Checks every rule against the student's details (forward chaining) |
| **User Interface** | `app.py` (web) and `cli.py` (terminal) | Takes input and shows results |
| **Explanation Facility** | Results page | Shows which conditions were met and which were not |

**Example rule:**
> IF income is up to Rs 4.5 lakh AND CGPA is at least 8.0 AND level is Undergraduate or Postgraduate, THEN the student is eligible for the Central Sector Merit-cum-Means Scholarship.

## 📋 Scholarships in the Knowledge Base

| No. | Scholarship | Conditions |
|---|---|---|
| 1 | **Post-Matric Scholarship for SC Students** | Category SC, family income up to Rs 2.5 lakh, Undergraduate or Postgraduate |
| 2 | **Post-Matric Scholarship for ST Students** | Category ST, family income up to Rs 2.5 lakh, Undergraduate or Postgraduate |
| 3 | **Post-Matric Scholarship for OBC Students** | Category OBC, family income up to Rs 1 lakh, CGPA at least 6.0 |
| 4 | **Central Sector Merit-cum-Means Scholarship** | Family income up to Rs 4.5 lakh, CGPA at least 8.0, Undergraduate or Postgraduate |
| 5 | **Girl Child Higher Education Support** | Female, family income up to Rs 6 lakh, CGPA at least 6.5 |
| 6 | **Scholarship for Students with Disabilities** | Disability of 40% or more, family income up to Rs 8 lakh |
| 7 | **EWS / General Means-based Scholarship** | Category General or EWS, family income up to Rs 3 lakh, CGPA at least 7.0 |
| 8 | **Himachal Pradesh Domicile Merit Scholarship** | Domicile of Himachal Pradesh, CGPA at least 7.5, family income up to Rs 5 lakh |
| 9 | **Technical Education Excellence Award** | Enrolled in B.Tech / Engineering, CGPA at least 9.0 |

> ⚠️ **Note:** These scholarships and limits are **sample data for demonstration**. For real applications, check the current criteria on the official portals such as [scholarships.gov.in](https://scholarships.gov.in) or your state scholarship portal.

## 📁 Project Structure

```
Scholarship-Expert-System/
├── app.py              # Streamlit web interface
├── cli.py              # Terminal (command-line) version
├── engine.py           # Inference engine (rule checking logic)
├── scholarships.json   # Knowledge base (all scholarships and rules)
├── requirements.txt    # Python dependency (streamlit)
└── README.md           # This file
```




## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** (web interface)
- **JSON** (knowledge base)

## 👤 Author

**Dheeraj** ([@dheeraj00tech](https://github.com/dheeraj00tech))
