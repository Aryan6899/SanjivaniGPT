# SanjivaniGPT 🤖

> **Sanjivani University's AI Ecosystem** — a university-focused multimodal AI assistant being built for the **Inter-Departmental LLM Development Challenge 2026**.

## 🎯 Vision

SanjivaniGPT is designed as one AI platform for **students, faculty, and administrators**. It combines university knowledge, document understanding, RAG, campus information, academic events, and coding challenges in one interface.

## ✨ Planned Features

### AI Assistant
- 💬 Text chat
- 🧠 Retrieval-Augmented Generation (RAG)
- 📄 PDF reader
- 📚 PDF chat
- 🖼️ Image reader
- 🎤 Voice input
- 🔊 Text-to-Speech
- 🌍 English + Marathi + Hindi
- 📖 Source citations

### Campus & University
- 📍 Campus map and location information
- 📅 Events and academic calendar
- 👨‍🎓 Student mode
- 👨‍🏫 Faculty mode
- 🛡️ Admin mode

### Coding Challenge Platform
- 💻 Teacher-created daily coding challenges
- 🧪 Test cases and automatic evaluation
- 📝 Student code submissions
- 📊 Student performance tracking
- 📈 Faculty performance dashboard
- 🏆 Challenge history and scores

## 🧠 High-Level Architecture

```text
                           SanjivaniGPT
                                │
                    ┌───────────┴───────────┐
                    │                       │
              React Frontend          FastAPI Backend
                    │                       │
          ┌─────────┼─────────┐     ┌───────┼────────┐
          │         │         │     │       │        │
        Chat     Campus    Coding  RAG     Auth    Services
          │       Map     Tests     │
          │         │         │     ├── PDF / Documents
          │         │         │     ├── Embeddings
          │         │         │     ├── Retrieval
          │         │         │     ├── LLM
          │         │         │     ├── Vision
          │         │         │     └── Speech
          │         │         │
          └─────────┴─────────┴───────────┐
                                         │
                              Database + Vector Store
```

## 🏗️ Planned Repository Structure

```text
SanjivaniGPT/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   │   ├── rag/
│   │   │   ├── llm/
│   │   │   ├── embeddings/
│   │   │   ├── pdf/
│   │   │   ├── vision/
│   │   │   ├── speech/
│   │   │   └── coding/
│   │   ├── database/
│   │   ├── utils/
│   │   ├── config.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── context/
│   └── package.json
│
├── rag/
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── retrieval/
│   └── evaluation/
│
├── data/
│   ├── documents/
│   ├── images/
│   ├── campus/
│   └── challenges/
│
├── tests/
├── docs/
└── scripts/
```

## 🛠️ Planned Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React + Vite | Web interface |
| Backend | Python + FastAPI | API and application logic |
| Database | PostgreSQL | Users, events, challenges, submissions |
| Vector Store | ChromaDB initially | RAG retrieval |
| RAG | Python RAG pipeline | University knowledge retrieval |
| PDF | PyMuPDF | PDF text extraction |
| Maps | React Leaflet + OpenStreetMap | Campus map |
| Testing | Pytest + frontend tests | Quality assurance |

The exact LLM, embedding model, speech provider, and deployment platform will be selected during implementation based on cost, quality, privacy, and the competition demo requirements.

## 🚀 Development Roadmap

### Phase 1 — Foundation
1. Repository and professional structure
2. FastAPI backend
3. React frontend
4. Frontend ↔ backend connection
5. Environment configuration
6. Health check and initial tests

### Phase 2 — AI + RAG
1. Basic AI chat
2. PDF ingestion
3. Text cleaning and chunking
4. Embeddings
5. Vector database
6. Retrieval
7. RAG generation
8. Source citations

### Phase 3 — Multimodal AI
1. PDF chat
2. Image reader
3. Voice input
4. Text-to-Speech
5. English / Marathi / Hindi

### Phase 4 — University Ecosystem
1. Authentication and roles
2. Student / Faculty / Admin dashboards
3. Campus map
4. Events
5. Academic calendar

### Phase 5 — Coding Challenge Platform
1. Challenge database
2. Faculty challenge creation
3. Student coding interface
4. Test cases
5. Code execution and evaluation
6. Submission history
7. Faculty performance dashboard

### Phase 6 — Competition Readiness
1. Security review
2. RAG evaluation
3. Automated tests
4. UI/UX refinement
5. Documentation
6. Demo dataset
7. Live demonstration preparation

## 📚 Competition

**Inter-Departmental LLM Development Challenge 2026**  
Theme: **Build Sanjivani's Own Large Language Model (LLM)**

Expected deliverables include a domain-specific AI assistant, knowledge base/dataset, RAG framework, functional prototype, technical documentation, and live demonstration.

## 👨‍💻 Development Philosophy

SanjivaniGPT will be built incrementally. Every major feature will be:

1. Designed
2. Explained
3. Implemented
4. Tested
5. Documented
6. Committed to GitHub

The goal is not only to make the application work, but also to make the architecture understandable and defensible during the competition evaluation.

## 👤 Project Lead

**Aryan Jadhav**  
Sanjivani University — IMTech

## 📄 License

MIT License. See [LICENSE](LICENSE).
