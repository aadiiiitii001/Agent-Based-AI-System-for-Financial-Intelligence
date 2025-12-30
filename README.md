# 🧠 Enterprise Agent-Based Financial Intelligence System

An **agent-based AI system** designed for **financial risk analysis, compliance monitoring, and decision support**, built using modern backend engineering practices and secure AI orchestration.

This project demonstrates how **multi-agent AI systems** can be safely deployed in **finance-grade environments** using **MCP (Model Context Protocol)**, audit logging, and containerized infrastructure.

---

## 🚀 Why This Project Matters (Market Relevance)

This system aligns directly with **current IT & finance trends**:

- Agent-based AI systems (used in trading, risk, compliance)
- Secure AI tool orchestration (MCP-style governance)
- Explainable AI (XAI) for financial decisions
- Cloud-ready microservice architecture
- Auditability & compliance-first design

---

## 🏗️ System Architecture

### 🔹 Core Agents
- **Orchestrator Agent**
  - Routes queries to specialized agents
  - Aggregates structured responses

- **Risk Agent**
  - Evaluates market risk & volatility
  - Produces explainable risk scores

- **Compliance Agent**
  - Detects regulatory & compliance concerns
  - Designed for RAG / PDF analysis extension

### 🔹 MCP Server
- Centralized tool execution layer
- Enforces security, access control & auditability
- Prevents direct agent-tool interaction

---

## 📂 Project Structure
```text
finance-agent-ai/
├── agents/ # AI agents (Risk, Compliance, Orchestrator)
├── api/ # FastAPI backend
├── mcp_server/ # MCP tool governance layer
├── db/ # Database models & audit logs
├── utils/ # Logging, security, helpers
├── tests/ # Unit tests
├── docker/ # Docker & docker-compose
├── requirements.txt
└── README.md
```
---

## 🛠️ Tech Stack

### Backend
- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **SQLite (PostgreSQL-ready)**

### AI & Orchestration
- Agent-based architecture
- MCP (Model Context Protocol)
- Explainable decision outputs

### DevOps
- Docker & Docker Compose
- Environment-agnostic deployment

### Testing
- Pytest-based unit tests

---

## 🔐 Security & Compliance Design

- No agent accesses tools directly
- All executions routed via MCP Server
- Audit logs stored for:
  - Agent name
  - Tool usage
  - Payload
  - Timestamp
- Input sanitization applied before processing

📌 **Finance-ready design principle**:  
> “AI systems must be explainable, auditable, and governed.”

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/aadiiiitii001/finance-agent-ai.git
cd finance-agent-ai
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Initialize Database
```bash
python db/init_db.py
```

### 4️⃣ Run API Server
```bash
uvicorn api.main:app --reload
```

### API will be available at:
```bash
http://localhost:8000
```

### 🐳 Run with Docker
```bash
docker-compose up --build
```

### 🧪 Run Tests
```bash
pytest
```

### 📊 Example Use Case

Input Query
```bash
"Analyze Tesla stock risk and compliance concerns"
```

### System Output
- Risk score with volatility explanation
- Compliance flags (if any)
- Structured, explainable decision summary

### 📈 Future Enhancements
- PostgreSQL integration
- RAG-based compliance document analysis
- Real-time market data ingestion
- ML-based risk scoring models
- Role-based access control (RBAC)

### 👤 Author
```bash
Aditi Nayak
Software Engineer | AI & Backend Systems
Focused on secure, explainable AI for enterprise finance
```
