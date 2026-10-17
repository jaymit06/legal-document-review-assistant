import ollama, sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schemas import RiskAnalyzerOutput, SummarizerOutput

MODEL = "llama3.1:8b"

def compute_risk_score(risk_output: RiskAnalyzerOutput) -> str:
    # computed in code, not trusted to the LLM — more reliable
    levels = [c.risk_level for c in risk_output.flagged_clauses]
    if "high" in levels:
        return "high"
    elif "medium" in levels:
        return "medium"
    return "low"

def summarize(risk_output: RiskAnalyzerOutput) -> SummarizerOutput:
    with open("prompts/summarizer_prompt.txt") as f:
        system_prompt = f.read()

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": risk_output.model_dump_json()}
        ]
    )
    raw = response["message"]["content"].strip().replace("```json", "").replace("```", "").strip()
    result = SummarizerOutput.model_validate_json(raw)
    result.overall_risk_score = compute_risk_score(risk_output)  # override with the reliable version
    return result