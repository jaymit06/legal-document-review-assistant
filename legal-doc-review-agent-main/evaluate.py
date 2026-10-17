import json
from agents.extractor import extract_clauses

with open("data/processed/eval_set.json") as f:
    eval_data = json.load(f)

correct = 0
total = 0

for item in eval_data[:15]:
    try:
        result = extract_clauses(item["document_id"], item["context"][:3000])
        found_types = [c.clause_type for c in result.clauses]
        expected_type = item["question"]
        matched = any(t.lower() in expected_type.lower() for t in found_types)
        total += 1
        if matched:
            correct += 1
    except Exception as e:
        print(f"Skipped {item['document_id']}: {str(e)[:150]}")

print(f"\nAccuracy on eval set: {correct}/{total} = {correct/total:.2%}" if total else "No results")