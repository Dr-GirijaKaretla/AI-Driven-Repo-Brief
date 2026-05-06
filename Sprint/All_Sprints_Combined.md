
# 🧭 AI Portfolio Automation — Sprint Plan
Version: 1.0  
Prepared for: Dr Girija  
Date: 06 May 2026  

## Sprints Overview
- Sprint 1: Environment & Infrastructure Setup  
- Sprint 2: Portfolio Repo Architecture  
- Sprint 3: CI/CD Workflows  
- Sprint 4: AI Logic, RAG & Resume Generation  



# 🧱 EPICS

### Epic 1 — Environment & Infrastructure Setup
### Epic 2 — Portfolio Repository Architecture
### Epic 3 — CI/CD Automation
### Epic 4 — AI Logic & RAG Layer
### Epic 5 — Testing, Deployment & Validation



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



# 🗂️ PROJECT TIMELINE

| Phase | Duration | Description |
|-------|----------|-------------|
| Setup | 2 days | Keys, AWS, GitHub |
| Architecture | 1 day | Repo structure |
| CI/CD | 2 days | Workflows |
| Python Scripts | 3 days | Summariser, KB, RAG |
| Testing | 2 days | Unit + integration |
| Deployment | 1 day | End-to-end run |



# 🧨 RISKS & MITIGATIONS

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM API limits | Medium | Use Groq |
| AWS free tier limits | Low | Use S3 + DynamoDB |
| PAT expiry | Medium | Rotate tokens |
| Incorrect summaries | Medium | Approval workflow |
