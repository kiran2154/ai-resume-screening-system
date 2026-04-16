"""
main.py
--------
Entry point for the AI Resume Screening System.

Pipeline Flow:
    Resume → Skill Extraction → Matching → Scoring → Explanation → Tracing

LangSmith tracing is enabled via environment variables in .env.
Every chain invocation is automatically logged as a traced run in LangSmith.

Usage:
    python main.py
"""

import os
from dotenv import load_dotenv

# ── Load environment variables (.env file) ────────────────────────────────────
load_dotenv()

# Validate critical env vars before importing LangChain components
_required_vars = ["OPENAI_API_KEY", "LANGCHAIN_API_KEY"]
for var in _required_vars:
    if not os.getenv(var):
        raise EnvironmentError(
            f"Missing required environment variable: {var}\n"
            "Please copy .env.example to .env and fill in your API keys."
        )

# LangSmith tracing must be set before any LangChain imports
os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
os.environ.setdefault("LANGCHAIN_PROJECT", "ai-resume-screener")

# ── Project imports ───────────────────────────────────────────────────────────
from langsmith import traceable                     # noqa: E402

from chains.screening_chains import (               # noqa: E402
    skill_extraction_chain,
    matching_chain,
    scoring_chain,
    explanation_chain,
)
from data.resumes import ALL_CANDIDATES, JOB_DESCRIPTION  # noqa: E402
from utils.display import (                         # noqa: E402
    print_section,
    print_candidate_header,
    build_result_summary,
    print_final_summary,
)


# ── Core pipeline function ────────────────────────────────────────────────────
@traceable(name="resume_screening_pipeline", tags=["assignment", "screening"])
def screen_candidate(candidate: dict, job_description: str) -> dict:
    """
    Run the full 4-step screening pipeline for a single candidate.

    Args:
        candidate: dict with keys "name" and "resume"
        job_description: the target job description string

    Returns:
        dict containing all pipeline outputs (profile, match, score, explanation)

    LangSmith will trace this function and all nested chain calls automatically.
    """
    name = candidate["name"]
    resume = candidate["resume"]

    # ── Step 1: Skill Extraction ─────────────────────────────────────────────
    print(f"\n  [Step 1] Extracting skills from {name}'s resume...")
    extracted_profile = skill_extraction_chain.invoke({"resume": resume})
    print_section("Extracted Profile", extracted_profile)

    # ── Step 2: Matching Logic ────────────────────────────────────────────────
    print(f"\n  [Step 2] Matching {name}'s profile against the job description...")
    match_analysis = matching_chain.invoke(
        {
            "job_description": job_description,
            "candidate_profile": extracted_profile,
        }
    )
    print_section("Match Analysis", match_analysis)

    # ── Step 3: Scoring ───────────────────────────────────────────────────────
    print(f"\n  [Step 3] Calculating fit score for {name}...")
    fit_score: int = scoring_chain.invoke({"match_analysis": match_analysis})
    print_section("Fit Score", f"{fit_score} / 100")

    # ── Step 4: Explanation ───────────────────────────────────────────────────
    print(f"\n  [Step 4] Generating explanation for {name}'s score...")
    explanation = explanation_chain.invoke(
        {
            "candidate_name": name,
            "fit_score": fit_score,
            "match_analysis": match_analysis,
        }
    )
    print_section("Explanation & Recommendation", explanation)

    return build_result_summary(
        name=name,
        profile=extracted_profile,
        match_analysis=match_analysis,
        fit_score=fit_score,
        explanation=explanation,
    )


# ── Main execution ────────────────────────────────────────────────────────────
def main():
    print("\n" + "█" * 70)
    print("  AI RESUME SCREENING SYSTEM — with LangSmith Tracing")
    print("  LangSmith Project:", os.environ.get("LANGCHAIN_PROJECT"))
    print("█" * 70)

    print("\nJob Description Preview:")
    print(JOB_DESCRIPTION[:300] + "...\n")

    all_results = []
    total = len(ALL_CANDIDATES)

    for idx, candidate in enumerate(ALL_CANDIDATES, start=1):
        print_candidate_header(candidate["name"], idx, total)
        result = screen_candidate(
            candidate=candidate,
            job_description=JOB_DESCRIPTION,
        )
        all_results.append(result)

    # ── Final leaderboard ─────────────────────────────────────────────────────
    print_final_summary(all_results)

    print("\n✅ All runs traced in LangSmith.")
    print(
        f"   View traces at: https://smith.langchain.com/projects/"
        f"{os.environ.get('LANGCHAIN_PROJECT', 'ai-resume-screener')}\n"
    )

    return all_results


if __name__ == "__main__":
    main()
