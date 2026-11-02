# Smart Scholarship Eligibility System

A rule-based **expert system** (AI Unit VI: Expert Systems) that tells a student which scholarships they qualify for and explains why.

## Expert system components
| Component | Where |
|---|---|
| Knowledge base | `scholarships.json` (IF-THEN rules) |
| Inference engine | `engine.py` (forward chaining over all rules) |
| User interface | `app.py` (Streamlit) or `cli.py` (terminal) |
| Explanation facility | Lists conditions passed and failed for every scholarship |

## Run
```
pip install -r requirements.txt
streamlit run app.py
```
No Streamlit? Run `python cli.py`.

## Adding a scholarship
Add a block to `scholarships.json`. No code changes needed.
Supported operators: `in`, `==`, `<=`, `>=`.

## Disclaimer
The scholarships and limits in the knowledge base are sample data for demonstration. Verify real criteria on scholarships.gov.in or the relevant state portal.
