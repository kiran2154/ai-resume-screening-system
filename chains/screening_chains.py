"""
chains/screening_chains.py
---------------------------
Modular LangChain LCEL chains for each stage of the resume screening pipeline.

Each chain follows the pattern:
    prompt | llm | output_parser

Chains are composed in main.py into the full pipeline.
LangSmith automatically traces each chain when LANGCHAIN_TRACING_V2=true.
"""

import re
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from prompts.templates import (
    skill_extraction_prompt,
    matching_prompt,
    scoring_prompt,
    explanation_prompt,
)

# ── Shared LLM instance ───────────────────────────────────────────────────────
# Using temperature=0 for deterministic, factual outputs (reduces hallucination)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ── Output Parser ─────────────────────────────────────────────────────────────
str_parser = StrOutputParser()


# ── Chain 1: Skill Extraction ─────────────────────────────────────────────────
# Input : {"resume": str}
# Output: str — structured profile (SKILLS, EXPERIENCE_YEARS, etc.)
skill_extraction_chain = skill_extraction_prompt | llm | str_parser


# ── Chain 2: Matching Logic ───────────────────────────────────────────────────
# Input : {"job_description": str, "candidate_profile": str}
# Output: str — match analysis (matched / missing skills, experience match, etc.)
matching_chain = matching_prompt | llm | str_parser


# ── Chain 3: Scoring ──────────────────────────────────────────────────────────
# Input : {"match_analysis": str}
# Output: int — fit score extracted from LLM response

def _parse_score(raw_output: str) -> int:
    """
    Parse the integer fit score from the LLM's raw text output.
    Falls back to 0 if no valid number is found.
    """
    match = re.search(r"FIT_SCORE[:\s]*(\d+)", raw_output)
    if match:
        return min(100, max(0, int(match.group(1))))
    # Fallback: grab the first standalone number in the response
    numbers = re.findall(r"\b(\d{1,3})\b", raw_output)
    if numbers:
        return min(100, max(0, int(numbers[0])))
    return 0

scoring_chain = scoring_prompt | llm | str_parser | RunnableLambda(_parse_score)


# ── Chain 4: Explanation ──────────────────────────────────────────────────────
# Input : {"candidate_name": str, "fit_score": int, "match_analysis": str}
# Output: str — human-readable explanation + recommendation
explanation_chain = explanation_prompt | llm | str_parser
