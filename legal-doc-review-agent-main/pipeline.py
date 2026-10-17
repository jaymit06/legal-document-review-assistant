from agents.extractor import extract_clauses 
from agents.risk_analyzer import analyze_risk
from agents.summarizer import summarize

def run_pipeline(document_id:str, contract_text:str) -> dict:
    extracted = extract_clauses(document_id, contract_text)
    risk = analyze_risk(extracted)
    summary = summarize(risk)
    return {
        "extracted": extracted.model_dump(),
        "risk": risk.model_dump(),
        "summary": summary.model_dump()
    }

if __name__ == "__main__":
    sample_text = "This Agreement shall remain confidential for 5 years. Either party may terminate with 30 days notice. This Agreement is governed by the laws of Delaware. Company shall indemnify Client without limitation."
    result = run_pipeline("demo_doc", sample_text)
    import json
    print(json.dumps(result, indent=2))