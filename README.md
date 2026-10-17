# Legal Document Review Assistant

An AI-assisted web application for preliminary contract review. The app uses a locally run language model to identify key clauses, flag potential risks, and produce a plain-English summary through a Streamlit interface.

> **Important:** This project is for educational and informational purposes only. It does not provide legal advice and is not a substitute for review by a qualified legal professional.

## Overview

Contracts can be lengthy and difficult to scan. The Legal Document Review Assistant explores how a language-model workflow can help users review text-based contracts by organising important clauses and highlighting areas that may deserve closer attention.

The application accepts a `.txt` contract, processes it through a sequence of specialised steps, and presents the results in a web interface.

## Features

- **Text-file input:** Upload a contract in `.txt` format.
- **Clause extraction:** Identify relevant contract clauses and organise the extracted information.
- **Risk analysis:** Flag potential concerns and missing or unclear provisions for further review.
- **Plain-English summary:** Generate a concise overview of the contract and its notable points.
- **Structured outputs:** Use Pydantic schemas to validate the shape of model-generated data.
- **Overall risk label:** Combine clause-level risk labels into an overall risk indication using deterministic Python logic.

The review focuses on clause categories such as confidentiality, termination, governing law, indemnification, and non-compete provisions, depending on what is present in the input document.

## How It Works

The application follows a sequential processing pipeline:

1. **Upload:** The user uploads a text-based contract through Streamlit.
2. **Clause extraction:** The extractor identifies and structures relevant clauses.
3. **Risk analysis:** The risk analyser examines the extracted clauses for potential issues.
4. **Summarisation:** The summariser turns the findings into a readable overview.
5. **Results:** The interface displays the extracted information, risk observations, and summary.

### High-level architecture

```text
Text contract (.txt)
        |
        v
Streamlit interface
        |
        v
Clause Extractor
        |
        v
Risk Analyzer
        |
        v
Summarizer
        |
        v
Structured review results
```

## Tech Stack

- **Python** — application logic and pipeline orchestration
- **Streamlit** — interactive web interface
- **Ollama** — local language-model runtime
- **Llama 3.1 8B** — language model used for analysis and summarisation
- **Pydantic** — validation of structured outputs
- **JSON** — structured data exchanged between processing steps

## Getting Started

### Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible Python version supported by the dependencies
- [Ollama](https://ollama.com/)
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/jaymit06/legal-document-review-assistant.git
cd legal-document-review-assistant
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If the repository includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If it does not, install the packages used by the project (at minimum, Streamlit, Ollama's Python client if used by the code, and Pydantic) according to the imports in the source files.

### 4. Download the model

Make sure Ollama is installed and running, then pull the model:

```bash
ollama pull llama3.1:8b
```

The model runs locally through Ollama. The first download may take some time and requires sufficient disk space and system memory.

### 5. Run the application

From the project directory, run:

```bash
streamlit run app.py
```

Streamlit will print a local URL in the terminal, usually `http://localhost:8501`. Open that address in your browser.

> If the entry-point file in your downloaded source has a different name, use that filename in the `streamlit run` command.

## Example Workflow

1. Start the app.
2. Upload a `.txt` contract.
3. Run the review.
4. Read the extracted clauses, potential risk flags, and plain-English summary.
5. Use the findings as a checklist for further manual review.

## Limitations

- The current input workflow is designed for `.txt` files; PDF and Word support may require additional parsing.
- Language-model outputs can omit, misinterpret, or incorrectly classify clauses.
- Risk labels are preliminary indicators and may not reflect the legal significance of a clause in its full context.
- Results can vary with document wording, length, and model behaviour.
- The tool does not replace jurisdiction-specific legal analysis or professional legal advice.

## Future Improvements

- Add PDF and Word document ingestion.
- Improve handling of long contracts through chunking and context management.
- Expand clause categories and configurable review criteria.
- Add stronger error handling and clearer feedback for unsupported or malformed inputs.
- Evaluate extraction and risk detection with labelled examples and metrics such as precision, recall, and F1-score.
- Support comparisons between contract versions and more consistent multi-document review.

## Academic Context

This project was developed as part of B.Tech Data Science coursework for the 2026–2027 academic year.

**Team**
- Jaymit Shriyan
- Kriday Thakkar
- Saai Sankhe

## Disclaimer

This application is an academic project intended to demonstrate an AI-assisted document-review workflow. It may produce incomplete or inaccurate results. Do not rely on its output as legal advice or use it as the sole basis for a legal decision. Have important contracts reviewed by a qualified legal professional.

## License

No license has been specified yet. Unless a license is added to this repository, reuse and redistribution are not automatically granted.
