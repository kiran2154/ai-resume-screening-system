"""
data/resumes.py
----------------
Sample resume data for three candidate profiles:
  - Strong candidate  (highly qualified)
  - Average candidate (partially qualified)
  - Weak candidate    (underqualified)

Each resume is stored as a plain-text string that mimics a real CV.
"""

JOB_DESCRIPTION = """
Position: Data Scientist
Company: TechCorp Analytics

We are looking for an experienced Data Scientist to join our team.

Required Skills:
- Python (NumPy, Pandas, Scikit-learn)
- Machine Learning (regression, classification, clustering)
- Deep Learning (TensorFlow or PyTorch)
- SQL and database querying
- Data visualization (Matplotlib, Seaborn, or Plotly)
- Experience with MLflow or similar experiment-tracking tools
- Strong understanding of statistics and probability

Nice to Have:
- NLP / LLM experience
- Cloud platforms (AWS, GCP, or Azure)
- Docker / containerization
- Experience with LangChain or similar LLM frameworks

Experience Required: 2+ years in a data science or ML role
Education: Bachelor's degree in Computer Science, Statistics, or related field
"""

# ── Strong Candidate ─────────────────────────────────────────────────────────
STRONG_CANDIDATE = {
    "name": "Ananya Sharma",
    "resume": """
Ananya Sharma
Email: ananya.sharma@email.com | LinkedIn: linkedin.com/in/ananyasharma
Location: Bengaluru, India

SUMMARY
Data Scientist with 4 years of experience building end-to-end ML pipelines and
deploying models in production. Passionate about NLP and LLM-based systems.

SKILLS
- Languages: Python, SQL, R
- ML Libraries: Scikit-learn, TensorFlow, PyTorch, XGBoost
- Data Tools: NumPy, Pandas, Matplotlib, Seaborn, Plotly
- MLOps: MLflow, Docker, GitHub Actions
- Cloud: AWS (SageMaker, S3, Lambda), GCP (BigQuery)
- NLP / GenAI: HuggingFace Transformers, LangChain, OpenAI API
- Databases: PostgreSQL, MySQL, MongoDB

EXPERIENCE
Senior Data Scientist — DataMinds Pvt. Ltd. (Jan 2022 – Present)
- Built a customer churn prediction model (XGBoost) achieving 91% AUC.
- Developed an NLP pipeline using BERT for sentiment analysis on 5M reviews.
- Led migration of ML workflows to AWS SageMaker; reduced inference latency by 40%.
- Implemented MLflow for experiment tracking across 3 product teams.
- Mentored 2 junior data scientists.

Data Scientist — Quantify Analytics (Jun 2020 – Dec 2021)
- Designed regression and classification models for demand forecasting.
- Created interactive dashboards with Plotly Dash for C-suite reporting.
- Automated ETL pipelines using Python and PostgreSQL.

EDUCATION
B.Tech, Computer Science — IIT Roorkee (2016–2020) | CGPA: 8.9 / 10

PROJECTS
- LLM-powered Resume Screener: Built with LangChain + GPT-4 (personal project).
- Real-time fraud detection system deployed on AWS Lambda.
""",
}

# ── Average Candidate ─────────────────────────────────────────────────────────
AVERAGE_CANDIDATE = {
    "name": "Rohan Mehta",
    "resume": """
Rohan Mehta
Email: rohan.mehta@email.com
Location: Pune, India

SUMMARY
Aspiring Data Scientist with 1.5 years of experience in data analysis and basic
machine learning. Comfortable with Python and SQL.

SKILLS
- Languages: Python, SQL
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib
- Tools: Jupyter Notebook, Excel, Tableau
- Databases: MySQL

EXPERIENCE
Data Analyst — InfoSoft Solutions (Jul 2022 – Present)
- Performed exploratory data analysis on sales datasets using Pandas.
- Built a linear regression model to forecast monthly revenue.
- Created Tableau dashboards for the marketing team.
- Wrote SQL queries to extract and clean data from MySQL databases.

Intern — StartUpX (Jan 2022 – Jun 2022)
- Assisted senior analysts with data cleaning and feature engineering.
- Learned basics of Scikit-learn and built a simple classification model.

EDUCATION
B.Sc, Statistics — University of Pune (2018–2021) | 72%

PROJECTS
- House Price Prediction using Linear Regression (Kaggle).
- Customer Segmentation using K-Means Clustering.
""",
}

# ── Weak Candidate ────────────────────────────────────────────────────────────
WEAK_CANDIDATE = {
    "name": "Priya Verma",
    "resume": """
Priya Verma
Email: priya.verma@email.com
Location: Jaipur, India

SUMMARY
Recent graduate looking for an opportunity in the IT sector. Eager to learn new
technologies. Background in business administration.

SKILLS
- Microsoft Office (Word, Excel, PowerPoint)
- Basic internet research
- Communication and teamwork
- Some exposure to Python during online course (basics only)

EXPERIENCE
Office Assistant — Local Travel Agency (Apr 2023 – Present)
- Managed customer inquiries and bookings via phone and email.
- Maintained spreadsheets for daily revenue tracking in Excel.

EDUCATION
BBA, Business Administration — Rajasthan University (2019–2022) | 65%

CERTIFICATIONS
- Python for Beginners — Coursera (2023) [completed Week 1–3 only]

PROJECTS
- None listed.
""",
}

ALL_CANDIDATES = [STRONG_CANDIDATE, AVERAGE_CANDIDATE, WEAK_CANDIDATE]
