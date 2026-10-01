# 🤖 AI Research Assistant

An AI-powered research assistant built with **Python, LangChain, Ollama, and the GitHub REST API**.

The application retrieves live GitHub repository information, extracts the relevant structured data, and uses a locally hosted LLM to generate grounded research answers.

---

## 🎯 Project Objective

The goal of this project is to understand how an AI application can combine:

- External APIs
- Structured data
- LLMs
- Prompt engineering
- Data validation
- Error handling
- Modular Python application design

The project is intentionally kept small and focused on the core AI engineering concepts.

---

## 🏗️ Architecture

```text
User
 │
 │ Repository name
 ▼
GitHub REST API
 │
 │ JSON response
 ▼
API Response
 │
 │ Validate + extract
 ▼
Structured Research Data
 │
 │
 │ User question
 ▼
Local LLM — Llama 3.2
 │
 ▼
Grounded Research Answer
```

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Application development |
| requests | HTTP/API communication |
| GitHub REST API | Live repository information |
| LangChain | LLM application framework |
| Ollama | Local LLM runtime |
| Llama 3.2 3B | Local language model |

---

## 📁 Project Structure

```text
AI Research Assistant/
│
├── app/
│   └── research_assistant.py
│
├── notebooks/
│   └── 01_api_research.ipynb
│
├── data/
│
├── README.md
│
└── requirements.txt
```

---

## 🔄 Application Flow

### 1. User provides a repository

Example:

```text
microsoft/semantic-kernel
```

### 2. Application calls GitHub API

```python
response = requests.get(url, timeout=10)
```

### 3. API returns JSON

The response contains repository information such as:

- Repository name
- Description
- Stars
- Forks
- Programming language
- Owner

### 4. JSON is converted into Python data

```python
data = response.json()
```

The JSON response becomes a Python dictionary.

### 5. Required information is extracted

Instead of sending the entire API response to the LLM, the application creates a smaller structured object:

```python
research_data = {
    "repository": data["full_name"],
    "description": data["description"],
    "stars": data["stargazers_count"],
    "forks": data["forks_count"],
    "language": data["language"],
    "owner": data["owner"]["login"],
}
```

### 6. User asks a question

Example:

```text
What programming language does this repository use?
```

### 7. LLM generates the answer

The structured repository information and user question are passed to the local LLM.

The prompt instructs the model to use **only the supplied information**.

---

## 🧠 Key Concepts Learned

### HTTP GET

Used to request information from an API.

```python
requests.get(url)
```

### HTTP Status Codes

Examples:

```text
200 → Success
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Server Error
```

### JSON

APIs commonly return structured JSON data.

Example:

```json
{
    "name": "langchain",
    "language": "Python",
    "stars": 147335
}
```

### Nested JSON

JSON objects can contain other objects.

Example:

```json
{
    "owner": {
        "login": "langchain-ai"
    }
}
```

Accessed in Python using:

```python
data["owner"]["login"]
```

### Grounding

The LLM is instructed to answer using only the information supplied by the application.

This helps reduce unsupported answers, but **does not guarantee zero hallucinations**.

### Validation

The application checks whether expected fields exist before using the API data.

### Error Handling

The application handles:

- Repository not found
- Non-success API responses
- Network errors
- Request timeout

### Modular Design

The application separates responsibilities into functions:

```text
get_repository_data()
        ↓
extract_research_data()
        ↓
create_llm()
        ↓
ask_llm()
        ↓
main()
```

This makes the application easier to test, debug, and extend.

---

## ▶️ How to Run

### Prerequisites

Make sure Ollama is running and the required model is available:

```powershell
ollama list
```

The project currently uses:

```text
llama3.2:3b
```

### Run the application

From the project root:

```powershell
py -3.14 app\research_assistant.py
```

The application will ask:

```text
Enter GitHub repository (owner/name):
```

Example:

```text
microsoft/semantic-kernel
```

Then:

```text
What would you like to know about this repository?
```

Example:

```text
What programming language does this repository use?
```

---

## 🧪 Example

### Input

```text
Repository:
langchain-ai/langchain

Question:
How many stars does this repository have?
```

### Process

```text
GitHub API
    ↓
Repository JSON
    ↓
Extract stargazers_count
    ↓
Structured research data
    ↓
Llama 3.2
```

### Output

The LLM generates a natural-language answer based on the supplied repository information.

---

## ⚠️ Current Limitations

This is an MVP and intentionally has a limited scope.

Currently:

- It works with GitHub repositories.
- It uses one external API.
- It extracts a fixed set of repository fields.
- It uses a local LLM.
- It does not yet use multiple tools.
- It does not have a web UI.
- It does not have a formal evaluation pipeline.
- It does not maintain research history.

---

## 🚀 Future Improvements

Potential future extensions include:

```text
Current Project
      ↓
Multiple APIs
      ↓
Tool Selection
      ↓
Multi-Tool Agent
      ↓
Agentic Research Assistant
```

Possible tools could include:

- GitHub API
- News API
- Weather API
- Search API
- Documentation API

The next major evolution is to move from a single-tool application toward a **multi-tool AI agent**.

---

## 🎓 AI Engineering Concepts Practiced

This project demonstrates:

- REST API integration
- HTTP requests
- JSON parsing
- Nested data extraction
- Data validation
- Error handling
- Timeout handling
- Prompt construction
- Grounded LLM generation
- Local LLM inference
- LangChain
- Ollama
- Modular Python design

---

## 📌 Project Status

**Status: MVP Complete ✅**

Completed:

- GitHub API integration
- JSON parsing
- Structured data extraction
- Local LLM integration
- User questions
- Grounded responses
- Error handling
- Timeout handling
- API response validation
- Modular Python structure

---

## 📚 Learning Progression

This project follows the AI Engineering roadmap:

```text
Project 0
Local AI Email Assistant
        ↓
Project 1
Enterprise Document Assistant / RAG
        ↓
Project 2
AI Research Assistant ← THIS PROJECT
        ↓
Project 3
Multi-Tool AI Agent
        ↓
Project 4
Agentic RAG
        ↓
Evaluation
        ↓
Production AI API
        ↓
Azure Deployment
```

---

## 👩‍💻 Author

**Rohini**

AI Engineering learning project