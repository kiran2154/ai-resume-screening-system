# 🤖 AI Resume Screening System with LangSmith Tracing

**Innomatics Technology Hub — Data Science Internship, February 2026**

---

## Overview

An end-to-end AI pipeline that evaluates candidate resumes against a job description using **LangChain** (LCEL), **OpenAI GPT-4o-mini**, and **LangSmith** for tracing and debugging.

### Pipeline Flow
```
Resume → Skill Extraction → Matching → Scoring → Explanation → LangSmith Tracing
```

---

## Project Structure

```
ai_resume_screener/
│
├── main.py                  # Entry point — runs the full pipeline
├── notebook.ipynb           # Jupyter Notebook version
├── requirements.txt         # Python dependencies
├── .env.example             # Template for environment variables
│
├── prompts/
│   ├── __init__.py
│   └── templates.py         # All 4 PromptTemplates (extraction, matching, scoring, explanation)
│
├── chains/
│   ├── __init__.py
│   └── screening_chains.py  # LCEL chains (prompt | llm | parser)
│
├── data/
│   ├── __init__.py
│   └── resumes.py           # 3 sample resumes + job description
│
└── utils/
    ├── __init__.py
    └── display.py           # Output formatting helpers
```

---

## Setup

### 1. Clone / download the project

```bash
git clone https://github.com/<your-username>/ai-resume-screener.git
cd ai-resume-screener
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API keys

```bash
cp .env.example .env
```

Edit `.env` and add your keys:

```env
OPENAI_API_KEY=sk-...
LANGCHAIN_API_KEY=ls__...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai-resume-screener
```

Get your **LangSmith API key** from: https://smith.langchain.com → Settings → API Keys

### 4. Run the pipeline

```bash
python main.py
```

Or open `notebook.ipynb` in Jupyter / VS Code.

---

## Pipeline Details

| Step | Chain | Input | Output |
|------|-------|-------|--------|
| 1 | `skill_extraction_chain` | Resume text | Skills, experience, tools |
| 2 | `matching_chain` | Profile + JD | Matched / missing skills |
| 3 | `scoring_chain` | Match analysis | Numeric score (0–100) |
| 4 | `explanation_chain` | Name + score + analysis | Human-readable explanation |

---

## LangSmith Tracing

LangSmith traces are enabled automatically when `LANGCHAIN_TRACING_V2=true`.

Each candidate run produces a **separate traced run** in LangSmith showing:
- All 4 pipeline steps
- Token usage per step
- Latency per step
- Inputs and outputs at each node

View your traces at: **https://smith.langchain.com**

---

## Evaluation Criteria Coverage

| Criterion | Implementation |
|-----------|---------------|
| Pipeline Design | 4-step LCEL pipeline in `chains/` |
| LangChain Implementation | PromptTemplate + LCEL + `.invoke()` |
| Scoring & Logic | Rubric-based scoring (0–100) |
| Explainability | Step 4 explanation chain |
| LangSmith Tracing | `@traceable` + env vars |
| Code Quality | Modular, commented, typed |
| Bonus | `@traceable` tags, structured output parsing |

---

## Bonus Features Implemented

- ✅ `@traceable` decorator with custom tags on `screen_candidate()`
- ✅ Structured output parsing (score extracted via regex from LLM output)
- ✅ Anti-hallucination rules in every prompt ("Do NOT assume skills not in resume")
- ✅ Leaderboard summary printed after all runs
