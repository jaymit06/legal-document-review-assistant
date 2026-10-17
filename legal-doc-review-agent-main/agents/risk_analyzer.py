import ollama, json, sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schemas import ExtractorOutput, RiskAnalyzerOutput

MODEL = "llama3.1:8b"

def analyze_risk(extractor_output: ExtractorOutput) -> RiskAnalyzerOutput:
    with open("prompts/risk_analyzer_prompt.txt") as f:
        system_prompt = f.read()

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": extractor_output.model_dump_json()}
        ]
    )
    raw = response["message"]["content"].strip().replace("```json", "").replace("```", "").strip()
    return RiskAnalyzerOutput.model_validate_json(raw)
