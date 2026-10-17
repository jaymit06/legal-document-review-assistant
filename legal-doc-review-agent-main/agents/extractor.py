import ollama, json, sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schemas import ExtractorOutput

MODEL = "llama3.1:8b"
ALLOWED_TYPES = {"Confidentiality", "Termination", "Governing Law", "Indemnification", "Non-Compete"}

def extract_clauses(document_id: str, contract_text: str) -> ExtractorOutput:
    with open("prompts/extractor_prompt.txt") as f:
        system_prompt = f.read()

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Document ID: {document_id}\n\nContract text:\n{contract_text}"}
        ]
    )
    raw = response["message"]["content"].strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    data = json.loads(raw)

    # Filter out any clauses with invalid types or missing required fields
    # instead of crashing the whole extraction
    clean_clauses = []
    for c in data.get("clauses", []):
        if c.get("clause_type") in ALLOWED_TYPES and all(k in c for k in ["text", "location", "confidence"]):
            clean_clauses.append(c)

    data["clauses"] = clean_clauses
    return ExtractorOutput.model_validate(data)

if __name__ == "__main__":
    sample_text = "This Agreement shall remain confidential for 5 years. Either party may terminate with 30 days notice. This Agreement is governed by the laws of Delaware."
    result = extract_clauses("test_doc_1", sample_text)
    print(result.model_dump_json(indent=2))