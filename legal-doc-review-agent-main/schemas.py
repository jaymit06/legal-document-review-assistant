from pydantic import BaseModel
from typing import Literal, List

class ExtractedClause(BaseModel):
    clause_type: Literal["Confidentiality", "Termination", "Governing Law", "Indemnification", "Non-Compete"]
    text: str
    location: str
    confidence: float

class ExtractorOutput(BaseModel):
    document_id: str
    clauses: List[ExtractedClause]

class FlaggedClause(BaseModel):
    clause_type: str
    text: str
    risk_level: Literal["low", "medium", "high"]
    reason: str

class RiskAnalyzerOutput(BaseModel):
    document_id: str
    flagged_clauses: List[FlaggedClause]
    missing_clauses: List[str]

class SummarizerOutput(BaseModel):
    document_id: str
    overall_risk_score: Literal["low", "medium", "high"]
    summary: str
    top_concerns: List[str]