import streamlit as st
from pipeline import run_pipeline

st.title("Legal Document Review Assistant")
st.caption("Upload a contract and get a summary along with risk analysis and flagged clauses.")

uploaded = st.file_uploader("Upload a contract (.txt)", type=["txt"])
if uploaded:
    text = uploaded.read().decode()
    with st.spinner("Running Extractor -> Risk Analyzer -> Summarizer..."):
        result = run_pipeline("uploaded_doc", text)

    st.subheader("Summary")
    st.write(result["summary"]["summary"])
    st.write(f"**Overall risk:** {result['summary']['overall_risk_score']}")

    st.subheader("Top Concerns")
    for concern in result["summary"]["top_concerns"]:
        st.write(f"- {concern}")

    st.subheader("Flagged Clauses")
    for c in result["risk"]["flagged_clauses"]:
        st.write(f"**{c['clause_type']}** ({c['risk_level']}): {c['reason']}")