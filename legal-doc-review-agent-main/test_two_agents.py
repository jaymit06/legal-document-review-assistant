from agents.extractor import extract_clauses
from agents.risk_analyzer import analyze_risk

sample_text = "This Agreement shall remain confidential for 5 years. Either party may terminate with 30 days notice. This Agreement is governed by the laws of Delaware. Company shall indemnify Client without limitation."

extracted = extract_clauses("test_doc_1", sample_text)
risk = analyze_risk(extracted)
print(risk.model_dump_json(indent=2))
