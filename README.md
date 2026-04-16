# 🤖 AI Resume Screening System with LangSmith Tracing

An end-to-end AI pipeline that evaluates candidate resumes against job descriptions using **LangChain (LCEL)**, **OpenAI GPT-4o-mini**, and **LangSmith** for observability and debugging.

---

## 🚀 Key Features

* 🔍 Automated **skill extraction** from resumes
* 🎯 Intelligent **job-resume matching**
* 📊 Quantitative **candidate scoring (0–100)**
* 🧠 Human-readable **explanations for decisions**
* 📈 Full pipeline **tracing with LangSmith**
* ⚙️ Modular architecture using **LangChain LCEL**

---

## 🧠 Pipeline Flow

```
Resume → Skill Extraction → Matching → Scoring → Explanation → LangSmith Tracing
```

---

## 📁 Project Structure

```
ai_resume_screener/
│
├── main.py
├── notebook.ipynb
├── requirements.txt
├── .env.example
│
├── prompts/
├── chains/
├── data/
└── utils/
```

---

## ⚙️ Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kiran2154/ai-resume-screening-system.git
cd ai-resume-screening-system
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API keys

```bash
cp .env.example .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_key_here
LANGCHAIN_API_KEY=your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai-resume-screener
```

---

### 4️⃣ Run the project

```bash
python main.py
```

---

## 📊 Pipeline Details

| Step | Chain            | Description                             |
| ---- | ---------------- | --------------------------------------- |
| 1    | Skill Extraction | Extracts skills, tools, experience      |
| 2    | Matching         | Compares candidate with job description |
| 3    | Scoring          | Generates fit score (0–100)             |
| 4    | Explanation      | Provides reasoning for score            |

---

## 📈 LangSmith Observability

* Full execution trace for each candidate
* Token usage & latency tracking
* Step-by-step debugging visibility

👉 View traces: https://smith.langchain.com

---

## 📸 Screenshots

> Add screenshots here to showcase LangSmith traces and outputs

```
Screenshots/
├── langsmith_trace_1.png
├── langsmith_trace_2.png
```

---

## 🧪 Sample Output

* Candidate Score: **78/100**
* Strengths: Python, ML, SQL
* Gaps: Deep Learning, MLOps

---

## 🏗️ Tech Stack

* **Python**
* **LangChain (LCEL)**
* **OpenAI API**
* **LangSmith**

---

## 🔒 Security Note

* API keys are stored in `.env` (not committed)
* `.gitignore` ensures sensitive data is excluded

---

## 🎯 Future Improvements

* Streamlit / Web UI
* Resume PDF parsing
* Candidate ranking dashboard
* Export results to CSV

---

## ⭐ If you found this useful

Give the repo a star ⭐
