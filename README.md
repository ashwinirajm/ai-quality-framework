# AI Quality Evaluation Framework

Enterprise-style AI Quality Assurance framework for validating Generative AI / LLM applications using automated evaluation techniques.

Built using:

* Python
* Pytest
* Gemini API
* Sentence Transformers
* GitHub Actions

---

# Features

* AI response relevancy validation
* Hallucination detection
* Prompt regression testing
* Latency testing
* Semantic similarity scoring
* Mock fallback mode
* CI/CD quality gates
* Automated AI evaluations

---

# Evaluation Types

| Evaluation            | Purpose                           | Metric             |
| --------------------- | --------------------------------- | ------------------ |
| Relevancy Testing     | Validate semantic correctness     | Cosine Similarity  |
| Hallucination Testing | Detect unsupported responses      | Context Similarity |
| Prompt Regression     | Detect prompt quality degradation | Semantic Score     |
| Latency Testing       | Validate response performance     | Response Time      |

---

# Project Structure

```text
ai-quality-framework/
│
├── datasets/
├── evaluators/
├── prompts/
├── services/
├── tests/
├── utils/
├── .github/workflows/
├── requirements.txt
└── README.md
```

---

# Setup

```bash id="mini1"
git clone <repo_url>
cd ai-quality-framework

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Create `.env`

```env id="mini2"
GOOGLE_API_KEY=your_api_key
```

Run tests:

```bash id="mini3"
pytest tests -s
```

---

# CI/CD Pipeline

GitHub Actions automatically:

* installs dependencies
* executes AI evaluation tests
* validates AI quality gates

Pipeline file:

```text
.github/workflows/ai-evals.yml
```

---

# Sample Test Execution Result

<img width="1441" height="798" alt="Screenshot 2026-05-10 at 6 05 14 PM" src="https://github.com/user-attachments/assets/2e037964-f4f4-4719-b6c7-609e8920dbe3" />

---

# Mock Mode

Framework supports:

* Live LLM testing
* Mock fallback testing

Benefits:

* deterministic test execution
* stable CI pipelines
* reduced API cost
* offline testing support

---
