"""
prompts/templates.py
---------------------
All LangChain PromptTemplates used by the resume screening pipeline.

Pipeline stages:
  1. skill_extraction_prompt  — extract skills / experience / tools from resume
  2. matching_prompt          — compare extracted profile against JD requirements
  3. scoring_prompt           — assign a numeric fit score (0–100)
  4. explanation_prompt       — produce a human-readable explanation

Design principles:
  - Clear, explicit instructions to minimise hallucination
  - Output constraints defined in every prompt
  - Only use information present in the provided text (no assumptions)
"""

from langchain_core.prompts import PromptTemplate

# ── 1. Skill Extraction ──────────────────────────────────────────────────────
SKILL_EXTRACTION_TEMPLATE = """
You are an expert HR assistant specialising in resume analysis.

Your task is to extract structured information from the resume below.

STRICT RULES:
- Extract ONLY information explicitly stated in the resume.
- Do NOT infer, assume, or hallucinate any skills or experience not written in the text.
- If a field has no data, write "None found".

Resume Text:
{resume}

Extract and return the following in this EXACT format:

SKILLS: <comma-separated list of technical skills>
EXPERIENCE_YEARS: <total years of relevant work experience as a number, e.g. 4>
EXPERIENCE_SUMMARY: <one-sentence summary of work experience>
TOOLS_AND_TECHNOLOGIES: <comma-separated list of tools, frameworks, and platforms>
EDUCATION: <highest degree and field>
PROJECTS: <comma-separated list of notable projects, or "None found">
"""

skill_extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template=SKILL_EXTRACTION_TEMPLATE,
)

# ── 2. Matching Logic ────────────────────────────────────────────────────────
MATCHING_TEMPLATE = """
You are a technical recruiter evaluating a candidate's fit for a job.

Job Description:
{job_description}

Candidate Profile (extracted from resume):
{candidate_profile}

STRICT RULES:
- Base your evaluation ONLY on the candidate profile provided above.
- Do NOT assume any skills that are not listed in the candidate profile.
- Be objective and systematic.

Perform a detailed match analysis:

REQUIRED_SKILLS_MATCHED: <list the required skills the candidate HAS>
REQUIRED_SKILLS_MISSING: <list the required skills the candidate LACKS>
NICE_TO_HAVE_MATCHED: <list the nice-to-have skills the candidate HAS>
EXPERIENCE_MATCH: <"Met", "Partially Met", or "Not Met"> — with one-line reason
EDUCATION_MATCH: <"Met" or "Not Met"> — with one-line reason
OVERALL_MATCH_LEVEL: <"Strong", "Average", or "Weak">
"""

matching_prompt = PromptTemplate(
    input_variables=["job_description", "candidate_profile"],
    template=MATCHING_TEMPLATE,
)

# ── 3. Scoring ───────────────────────────────────────────────────────────────
SCORING_TEMPLATE = """
You are an objective AI scoring system for candidate evaluation.

Based on the match analysis below, assign a single numeric fit score from 0 to 100.

Scoring Rubric:
- Required skills match    : up to 40 points
- Experience match         : up to 25 points
- Education match          : up to 10 points
- Nice-to-have skills match: up to 15 points
- Project relevance        : up to 10 points

Match Analysis:
{match_analysis}

STRICT RULES:
- Output ONLY the score as an integer between 0 and 100.
- Do NOT add any explanation in this step — just the number.
- Example valid output: 78

FIT_SCORE: <integer 0-100>
"""

scoring_prompt = PromptTemplate(
    input_variables=["match_analysis"],
    template=SCORING_TEMPLATE,
)

# ── 4. Explanation ───────────────────────────────────────────────────────────
EXPLANATION_TEMPLATE = """
You are an AI system that produces transparent, explainable hiring recommendations.

Candidate Name: {candidate_name}
Fit Score: {fit_score} / 100

Match Analysis:
{match_analysis}

Write a concise, professional explanation (3–5 sentences) for a recruiter that covers:
1. Why the candidate received this score.
2. Their key strengths relative to the role.
3. Their main gaps or weaknesses.
4. A clear recommendation: "Strongly Recommended", "Consider with Reservations", or "Not Recommended".

STRICT RULES:
- Do NOT invent skills or qualifications not mentioned in the match analysis.
- Be factual and constructive.
- End with the recommendation label on its own line.
"""

explanation_prompt = PromptTemplate(
    input_variables=["candidate_name", "fit_score", "match_analysis"],
    template=EXPLANATION_TEMPLATE,
)
