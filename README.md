
# 📘 AI‑Driven Git Repo Dashboard & Resume Automation Ecosystem  
## Business Requirements Document (BRD) + Functional & Technical Specification  
**Version:** 1.0  
**Prepared for:** Dr Girija  
**Date:** 06 May 2026  

---

## 🧭 1. Project Overview
This project builds a production‑ready, automated ecosystem that:

- Monitors all GitHub repositories owned by the user  
- Detects changes to project documentation  
- Alerts the user for approval  
- Generates AI‑optimised project summaries  
- Stores summaries in a central knowledge base  
- Uses RAG to generate and update an AI‑Engineer‑ready resume  
- Ensures the user’s portfolio is always current, accurate, and competitive  

---

## 🎯 2. Business Objectives
- Automate project summarisation  
- Maintain a single source of truth for project summaries  
- Auto‑generate resume sections tailored for AI engineering roles  
- Reduce manual effort and ensure consistency  
- Improve competitiveness in AI‑focused job applications  

---

## 🧩 3. Business Problems
- Manual resume updates are slow and inconsistent  
- No centralised knowledge base of skills and achievements  
- Recruiters struggle to understand the user’s AI capabilities  
- No automation linking GitHub activity to resume updates  

---

## 🏆 4. Success Metrics
| Metric | Target |
|--------|--------|
| Resume update time after repo change | < 5 minutes |
| Summary accuracy | > 90% |
| Manual intervention | Only approval step |
| Portfolio completeness | 100% repos summarised |
| Resume freshness | Updated within 24 hours |

---

## 👥 5. Stakeholders
- **Primary User:** Dr Girija  
- **System Components:** GitHub Actions, AWS, LLM APIs  
- **Consumers:** Recruiters, hiring managers, portfolio reviewers  

---

## ⚙️ 6. Functional Requirements

### 6.1 Repo Change Detection
- Detect `.md` file changes in any GitHub repo  
- Trigger CI/CD workflow on commit  

### 6.2 Approval Workflow
- Create GitHub Issue for approval  
- User responds with `/approve` or `/skip`  
- Workflow continues or exits accordingly  

### 6.3 Summarisation Engine
- Extract README.md and docs  
- Generate structured summary using LLM  
- Summary includes:  
  - One‑liner  
  - Tech stack  
  - AI/ML components  
  - Key contributions  
  - Impact  
  - Keywords  

### 6.4 Knowledge Base Update
- Store summaries in JSON + S3  
- Track metadata in DynamoDB  
- Maintain version history  

### 6.5 RAG Resume Generator
- Convert summaries into embeddings  
- Retrieve top AI‑relevant projects  
- Generate resume section  
- Update resume markdown file  

### 6.6 Notifications
- Notify user on:  
  - Repo change  
  - Summary generated  
  - Resume updated  

---

## 🔐 7. Non‑Functional Requirements

### 7.1 Performance
- Summaries generated within 30 seconds  
- Resume generation within 20 seconds  

### 7.2 Scalability
- Support 100+ repositories  
- Support future UI and API expansion  

### 7.3 Security
- All secrets stored in GitHub Secrets  
- IAM user with least privilege  
- No secrets logged  

### 7.4 Reliability
- Workflows retry on failure  
- Logs stored in S3  

### 7.5 Maintainability
- Modular Python scripts  
- Clear folder structure  
- Versioned summaries  

---

## 🏗️ 8. Technical Specification

### 8.1 Architecture Diagram (Textual)

GitHub Repos → GitHub Actions → Approval → Summariser → KB → RAG → Resume Generator → Portfolio Repo

### 8.2 Components
- GitHub Actions  
- AWS S3, DynamoDB, SNS  
- Groq, Gemini, HuggingFace  
- Chroma/OpenSearch  
- Python scripts  

---

## 🗂️ 9. Project Timeline

| Phase | Duration | Description |
|-------|----------|-------------|
| Setup | 2 days | Keys, AWS, GitHub |
| Architecture | 1 day | Repo structure |
| CI/CD | 2 days | All workflows |
| Python Scripts | 3 days | Summariser, KB, RAG |
| Testing | 2 days | Unit + integration |
| Deployment | 1 day | End‑to‑end run |
| Enhancements | Optional | UI, JD‑to‑resume |

Total: **11 days**.

---

## 📌 10. Version History
| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 06 May 2026 | Initial BRD + Specs + Timeline |
