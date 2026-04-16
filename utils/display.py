"""
utils/display.py
-----------------
Helper functions for formatting and printing pipeline results.
"""

from typing import Any


def print_section(title: str, content: Any) -> None:
    """Print a clearly delimited section with a title."""
    bar = "─" * 60
    print(f"\n{bar}")
    print(f"  {title}")
    print(bar)
    print(content)


def print_candidate_header(name: str, index: int, total: int) -> None:
    """Print a prominent header for each candidate run."""
    line = "═" * 70
    print(f"\n{line}")
    print(f"  CANDIDATE {index}/{total}: {name.upper()}")
    print(line)


def build_result_summary(
    name: str,
    profile: str,
    match_analysis: str,
    fit_score: int,
    explanation: str,
) -> dict:
    """
    Bundle all pipeline outputs into a structured result dict.
    This dict is returned by the main pipeline and can be serialised to JSON.
    """
    return {
        "candidate_name": name,
        "extracted_profile": profile,
        "match_analysis": match_analysis,
        "fit_score": fit_score,
        "explanation": explanation,
        "recommendation": _extract_recommendation(explanation),
    }


def _extract_recommendation(explanation: str) -> str:
    """Pull the final recommendation label from the explanation text."""
    labels = [
        "Strongly Recommended",
        "Consider with Reservations",
        "Not Recommended",
    ]
    for label in labels:
        if label.lower() in explanation.lower():
            return label
    return "See explanation"


def print_final_summary(results: list[dict]) -> None:
    """Print a ranked leaderboard table of all candidates."""
    sorted_results = sorted(results, key=lambda r: r["fit_score"], reverse=True)
    line = "═" * 70
    print(f"\n\n{line}")
    print("  FINAL SCREENING RESULTS — RANKED BY FIT SCORE")
    print(line)
    print(f"{'Rank':<6}{'Candidate':<25}{'Score':>7}{'  Recommendation'}")
    print("─" * 70)
    for rank, r in enumerate(sorted_results, 1):
        print(
            f"{rank:<6}{r['candidate_name']:<25}{r['fit_score']:>5}/100"
            f"  {r['recommendation']}"
        )
    print(line)
