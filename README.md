# 🏥 Healthcare Agentic AI Decision Support Platform

An end-to-end **Agentic AI Healthcare Decision Support System** that automates MRI authorization recommendations using **Retrieval-Augmented Generation (RAG)**, **Multi-Agent AI**, **Vector Search**, and **Evidence Grounding**.

The system retrieves relevant clinical guidelines and insurance policies, validates whether sufficient evidence exists, generates an explainable recommendation, and escalates unsupported cases for manual review.

---

# Features

* Multi-Agent AI Workflow
* Retrieval-Augmented Generation (RAG)
* Semantic Search using Vector Embeddings
* Clinical & Insurance Policy Retrieval
* Evidence Grounding Validation
* Hallucination Reduction
* Human-in-the-Loop Manual Review
* Explainable AI Recommendations
* REST APIs using FastAPI
* Modern React + Next.js Frontend

---

# Problem Statement

Healthcare providers often spend significant time reviewing clinical guidelines and insurance policies before determining whether advanced imaging, such as MRI, should be approved.

Traditional manual review suffers from:

* Time-consuming policy lookups
* Inconsistent decisions
* Limited explainability
* Risk of unsupported AI recommendations

This project demonstrates how Agentic AI can automate evidence retrieval while ensuring recommendations remain grounded in retrieved clinical and policy evidence.

---

# Solution Overview

The application performs the following workflow:

1. Accept patient information.
2. Retrieve relevant clinical guidelines.
3. Retrieve insurance policy documents.
4. Validate that retrieved evidence supports the requested condition.
5. Generate an explainable recommendation.
6. Verify the workflow using a Supervisor Agent.
7. Escalate unsupported cases for manual review.

---

# System Architecture

```
                    User

                      │

             React / Next.js UI

                      │

               FastAPI Backend

                      │

             Decision Service

                      │

     ┌─────────────────────────────────┐
     │                                 │
     ▼                                 ▼

 Intake Agent                  Decision Agent

                                       │

                              Tool Calling Service

                    ┌────────────┴─────────────┐

                    ▼                          ▼

          Clinical Retrieval          Policy Retrieval

                    │                          │

                    ▼                          ▼

              Qdrant Vector Database (RAG)

                    │

                    ▼

          Evidence Validation Agent

                    │

        YES ---------------------- NO

         │                         │

         ▼                         ▼

 Generate Recommendation     Manual Review

         │

         ▼

     Supervisor Agent

         │

         ▼

  Final Recommendation + Evidence
```

---

# Tech Stack

## Backend

* Python
* FastAPI
* Pydantic

## AI

* OpenAI GPT-4.1
* Retrieval-Augmented Generation (RAG)
* Multi-Agent AI
* Tool Calling
* Prompt Engineering
* Evidence Grounding
* Human-in-the-Loop Validation

## Vector Database

* Qdrant

## Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

## Frontend

* React
* Next.js
* TypeScript
* Tailwind CSS

---

# Agent Workflow

## Intake Agent

Responsible for:

* Validating incoming requests
* Structuring patient information
* Preparing workflow context

---

## Decision Agent

Responsible for:

* Calling retrieval tools
* Generating recommendations
* Producing reasoning
* Assigning confidence scores

---

## Supervisor Agent

Responsible for:

* Verifying workflow completion
* Confirming evidence validation
* Determining whether manual review is required

---

# AI Guardrails

To reduce hallucinations, the system implements multiple safety layers.

## Evidence Retrieval

Clinical recommendations are generated only after retrieving relevant clinical and insurance documents.

---

## Grounding Validation

The retrieved evidence must explicitly support the requested medical condition.

Example:

✅ Neck Pain

Evidence:

* Neck pain guideline
* MRI guideline

Result:

VERIFIED

---

❌ Eye Tumor

Evidence:

* Neck pain guideline

Result:

MANUAL REVIEW

---

## Human-in-the-Loop

If sufficient evidence is unavailable, the workflow automatically escalates the case for manual review instead of generating unsupported recommendations.

---

# API Endpoint

## POST

```
/decision
```

### Request

```json
{
  "condition": "Neck Pain",
  "duration_weeks": 17,
  "physical_therapy": true
}
```

### Response

```json
{
  "recommendation": "YES",
  "reasoning": "...",
  "confidence": "HIGH",
  "status": "VERIFIED",
  "evidence": [...],
  "tools_used": [...]
}
```

---

# Sample Test Cases

## Test 1 — Approved Recommendation

Condition

```
Neck Pain
```

Duration

```
17 Weeks
```

Physical Therapy

```
Yes
```

Expected

```
Status:
VERIFIED

Recommendation:
YES

Confidence:
HIGH
```

---

## Test 2 — Unsupported Condition

Condition

```
Eye Tumor
```

Expected

```
Status:
REVIEW REQUIRED

Recommendation:
MANUAL REVIEW
```

---

## Test 3 — Different Body Part

Condition

```
Arm Pain
```

Expected

```
Manual Review
```

---

## Test 4 — Unknown Condition

Condition

```
RandomDisease123
```

Expected

```
Manual Review
```

---

# Project Structure

```
healthcare-agentic-ai/

├── app/
│   ├── agents/
│   ├── api/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   └── workflows/
│
├── frontend/
│
├── data/
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# Running the Project

## Backend

```bash
python -m venv venv

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:3000
```

Backend:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# Future Improvements

* Docker & Docker Compose
* Cloud Deployment (Vercel + Render)
* Authentication & Role-Based Access
* Medical Knowledge Graph Integration
* LangGraph Workflow Orchestration
* Observability with LangSmith/OpenTelemetry
* Unit & Integration Testing
* Feedback Collection for Human Review
* Additional Clinical Specialties
* Hybrid Search (Semantic + Keyword)
* Metadata Filtering Enhancements
* Retrieval Evaluation Metrics

---

# Key Learnings

Through this project I gained hands-on experience with:

* Agentic AI System Design
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Prompt Engineering
* Multi-Agent Orchestration
* Tool Calling
* Evidence Grounding
* Hallucination Mitigation
* Explainable AI
* FastAPI Backend Development
* React + Next.js Frontend Development
* End-to-End AI Application Development

---

# License

This project is intended for educational and portfolio purposes.

It is **not intended for real-world medical diagnosis or clinical decision-making**. All recommendations should be reviewed by qualified healthcare professionals.
