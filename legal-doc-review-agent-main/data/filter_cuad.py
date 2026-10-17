import json
TARGET_CLAUSES = ["Confidentiality", "Termination", "Governing Law",
"Indemnification", "Non-Compete"]

def contains_target(question):
    return any(clause.lower() in question.lower() for clause in
TARGET_CLAUSES)
filtered = []
with open("data/raw/cuad_train.json") as f:
    for line in f:
        row = json.loads(line)
        if contains_target(row["question"]) and row["answers"]["text"]:
            filtered.append({
                "document_id": row["title"],
"context": row["context"],
"question": row["question"],
"answer": row["answers"]["text"][0]
})
print(f"Filtered down to {len(filtered)} labeled clause examples")
with open("data/processed/filtered_contracts.json", "w") as f:
    json.dump(filtered, f, indent=2)
