import os
import zipfile

# ---------------------------------------------------
# Resolve correct path to Sprint folder
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # AI-Driven-Repo-Brief/
SPRINT_FOLDER = os.path.join(BASE_DIR, "Sprint")        # AI-Driven-Repo-Brief/Sprint

os.makedirs(SPRINT_FOLDER, exist_ok=True)

# ---------------------------------------------------
# Sprint Plan Content Templates
# ---------------------------------------------------

SPRINT_DOC = """
# 🧭 AI Portfolio Automation — Sprint Plan
Version: 1.0  
Prepared for: Dr Girija  
Date: 06 May 2026  

## Sprints Overview
- Sprint 1: Environment & Infrastructure Setup  
- Sprint 2: Portfolio Repo Architecture  
- Sprint 3: CI/CD Workflows  
- Sprint 4: AI Logic, RAG & Resume Generation  
"""

EPICS = """
# 🧱 EPICS

### Epic 1 — Environment & Infrastructure Setup
### Epic 2 — Portfolio Repository Architecture
### Epic 3 — CI/CD Automation
### Epic 4 — AI Logic & RAG Layer
### Epic 5 — Testing, Deployment & Validation
"""

USER_STORIES = """
# 🧩 USER STORIES

US‑01: Configure API keys and secrets  
US‑02: Create AWS services  
US‑03: Create portfolio repo structure  
US‑04: Detect README changes  
US‑05: Approval workflow  
US‑06: LLM summariser  
US‑07: Knowledge base updater  
US‑08: Embedding generator  
US‑09: RAG resume generator  
US‑10: Logging and error tracking  
US‑11: End‑to‑end testing  
"""

ACCEPTANCE_CRITERIA = """
# ✔ ACCEPTANCE CRITERIA

## US‑04 — Detect README Changes
- Workflow triggers on .md changes  
- Issue created for approval  

## US‑06 — Summarisation Engine
- Summary includes one‑liner, tech stack, AI components, contributions, impact  
- Generated in < 30 seconds  

## US‑09 — Resume Generator
- RAG retrieves top AI projects  
- Resume generated in Markdown  
"""

TIMELINE = """
# 🗂️ PROJECT TIMELINE

| Phase | Duration | Description |
|-------|----------|-------------|
| Setup | 2 days | Keys, AWS, GitHub |
| Architecture | 1 day | Repo structure |
| CI/CD | 2 days | Workflows |
| Python Scripts | 3 days | Summariser, KB, RAG |
| Testing | 2 days | Unit + integration |
| Deployment | 1 day | End-to-end run |
"""

RISKS = """
# 🧨 RISKS & MITIGATIONS

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM API limits | Medium | Use Groq |
| AWS free tier limits | Low | Use S3 + DynamoDB |
| PAT expiry | Medium | Rotate tokens |
| Incorrect summaries | Medium | Approval workflow |
"""

JIRA_CSV = """Summary,Description,Issue Type
Configure API keys,Set up Groq/Gemini/HF keys,Task
Create AWS services,Create S3/DynamoDB/SNS,Task
Create repo structure,Set up portfolio repo,Task
Detect README changes,Implement workflow,Story
Approval workflow,GitHub Issue approval,Story
Summariser,Implement LLM summariser,Story
Knowledge base updater,Update JSON + S3,Story
Embedding generator,Generate embeddings,Story
RAG resume generator,Generate resume,Story
Logging,Implement logs,Task
End-to-end testing,Full system test,Story
"""

# ---------------------------------------------------
# Write files into Sprint folder
# ---------------------------------------------------

files = {
    "Sprints_Document.md": SPRINT_DOC,
    "Epics.md": EPICS,
    "User_Stories.md": USER_STORIES,
    "Acceptance_Criteria.md": ACCEPTANCE_CRITERIA,
    "Timeline.md": TIMELINE,
    "Risks_and_Mitigations.md": RISKS,
    "Jira_Import.csv": JIRA_CSV
}

for filename, content in files.items():
    path = os.path.join(SPRINT_FOLDER, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ---------------------------------------------------
# C. Create Combined Sprint Summary
# ---------------------------------------------------

combined_md = (
    SPRINT_DOC
    + "\n\n"
    + EPICS
    + "\n\n"
    + USER_STORIES
    + "\n\n"
    + ACCEPTANCE_CRITERIA
    + "\n\n"
    + TIMELINE
    + "\n\n"
    + RISKS
)

combined_path = os.path.join(SPRINT_FOLDER, "All_Sprints_Combined.md")

with open(combined_path, "w", encoding="utf-8") as f:
    f.write(combined_md)

# ---------------------------------------------------
# D. Create Sprint Dashboard README
# ---------------------------------------------------

dashboard = f"""
# 📊 Sprint Dashboard

Welcome to the **AI Portfolio Automation Sprint Dashboard**.

This folder contains all sprint documentation generated automatically.

---

## 📁 Sprint Files

- [Sprints_Document.md](Sprints_Document.md)
- [Epics.md](Epics.md)
- [User_Stories.md](User_Stories.md)
- [Acceptance_Criteria.md](Acceptance_Criteria.md)
- [Timeline.md](Timeline.md)
- [Risks_and_Mitigations.md](Risks_and_Mitigations.md)
- [Jira_Import.csv](Jira_Import.csv)
- [All_Sprints_Combined.md](All_Sprints_Combined.md)

---

## 📦 Download Full Sprint Pack

A ZIP file containing all sprint documents is available here:

👉 **Sprint_Plan.zip**

---

## 🗂 Project Timeline

{TIMELINE}

---

Generated automatically by `generate_sprints.py`.
"""

dashboard_path = os.path.join(SPRINT_FOLDER, "README.md")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(dashboard)

# ---------------------------------------------------
# Create ZIP file inside Sprint folder
# ---------------------------------------------------

zip_path = os.path.join(SPRINT_FOLDER, "Sprint_Plan.zip")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files_in_dir in os.walk(SPRINT_FOLDER):
        for file in files_in_dir:
            zipf.write(os.path.join(root, file),
                       arcname=os.path.relpath(os.path.join(root, file), SPRINT_FOLDER))

print("Sprint files, combined summary, dashboard, and ZIP created successfully!")
