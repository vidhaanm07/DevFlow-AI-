# DevFlow AI

> **Autonomous AI Software Development Workflow**

DevFlow AI is a multi-agent software engineering system that transforms a natural-language feature request into a structured development workflow.

Instead of asking a single AI model to understand requirements, inspect code, plan changes, implement them, and verify the result all at once, DevFlow AI separates the process into specialized AI agents.

```text
Feature Request
      ↓
Requirements Analyst
      ↓
Codebase Analyst
      ↓
Development Planner
      ↓
Developer Agent
      ↓
Verification Agent
      ↓
Final Development Report
```

---

## 1. Problem

Traditional AI coding assistants often depend heavily on a single conversational workflow.

A developer may need to:

* Explain the requirement
* Understand the existing codebase
* Decide which files need modification
* Create an implementation plan
* Write the code
* Review the changes
* Verify whether the implementation actually satisfies the requirement

This creates several problems:

* Poor separation of responsibilities
* Inconsistent planning
* Limited independent verification
* Difficulty maintaining a reliable development workflow
* Increased risk of incorrect or incomplete code changes

DevFlow AI addresses this by turning software development into an **agentic pipeline**.

---

## 2. Solution

DevFlow AI uses specialized agents, each responsible for a specific stage of development.

### Requirements Analyst

Converts the user's natural-language request into a structured software requirement.

It identifies:

* Objective
* Functional requirements
* Non-functional requirements
* Assumptions
* Ambiguities
* Acceptance criteria
* Edge cases

### Codebase Analyst

Investigates the existing project using developer tools.

It identifies:

* Relevant files
* Existing architecture
* Existing functionality
* Dependencies
* Potential conflicts
* Missing components
* Required modifications

### Development Planner

Converts the requirements and codebase analysis into an implementation plan.

The planner determines:

* Files to modify
* Files to create
* Dependencies
* API changes
* Database impact
* Implementation order
* Testing strategy
* Security considerations
* Risks
* Acceptance criteria

### Developer Agent

Executes the development plan using project-level tools.

The developer can:

* List files
* Read files
* Search source code
* Create files
* Replace files
* Update specific sections of files

This allows DevFlow AI to operate directly on the project rather than merely generating code in the chat.

### Verification Agent

Acts as an independent review stage.

It evaluates:

* Implementation correctness
* Integration
* Acceptance criteria
* Test evidence
* Remaining issues
* Potential risks

The verifier produces a final verification status such as:

```text
PASS
FAIL
```

and provides recommendations when improvements are required.

---

## 3. Architecture

```text
                         ┌─────────────────────┐
                         │    User Request     │
                         │ "Add a new feature" │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Requirements Agent  │
                         │                     │
                         │ Requirements        │
                         │ Acceptance Criteria │
                         │ Edge Cases          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Codebase Analyst   │
                         │                     │
                         │ Files               │
                         │ Architecture        │
                         │ Dependencies        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Development Planner │
                         │                     │
                         │ Implementation Plan │
                         │ Testing Strategy    │
                         │ Risks               │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Developer Agent   │
                         │                     │
                         │ Read / Search       │
                         │ Create / Update     │
                         │ Project Files       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Verification Agent  │
                         │                     │
                         │ Implementation      │
                         │ Integration         │
                         │ Tests               │
                         │ Acceptance Criteria │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Final DevFlow     │
                         │       Result        │
                         └─────────────────────┘
```

---

## 4. End-to-End Workflow

When the user enters a request such as:

```text
Add a health check endpoint to the FastAPI backend
that returns the application status and version.
```

DevFlow AI processes it through the following pipeline.

### Step 1 — Requirements Analysis

The request is converted into structured requirements.

Example:

```text
Feature:
Health Check Endpoint

Functional Requirements:
- Return application status
- Return application version

Acceptance Criteria:
- GET /health responds successfully
- Response contains status
- Response contains version
```

---

### Step 2 — Codebase Analysis

The Codebase Analyst investigates the existing project.

It determines:

```text
Relevant Files
    ↓
Existing Architecture
    ↓
Existing Functionality
    ↓
Required Changes
    ↓
Potential Conflicts
    ↓
Missing Components
```

The agent uses project tools rather than assuming the project structure.

---

### Step 3 — Development Planning

The planner receives the requirements and codebase analysis.

It generates a structured implementation plan containing:

```text
Feature Summary
Existing System
Files to Modify
Files to Create
Dependencies
API Changes
Database Changes
Implementation Order
Testing Strategy
Security Considerations
Risks
Acceptance Criteria
```

---

### Step 4 — Autonomous Development

The Developer Agent executes the plan.

The available developer tools provide controlled access to the project:

```text
list_files()
read_file()
write_file()
update_file()
search_code()
```

The tools are restricted to the project directory to prevent accidental access outside the codebase.

---

### Step 5 — Verification

After development, the Verification Agent independently reviews the result.

It checks:

```text
Implementation
      ↓
Integration
      ↓
Acceptance Criteria
      ↓
Testing Evidence
      ↓
Remaining Issues
      ↓
Final Status
```

This prevents the development agent from being the only judge of whether its own work was successful.

---

## 5. Example

### Input

```text
Add a health check endpoint to the FastAPI backend
that returns the application status and version.
```

### DevFlow Pipeline

```text
Requirements Analyst
        ↓
Requirements completed

Codebase Analyst
        ↓
Codebase analysis completed

Development Planner
        ↓
Development plan completed

Developer
        ↓
Implementation completed

Verification Agent
        ↓
Verification completed
```

### Example API Response

```json
{
  "status": "online",
  "version": "1.0.0"
}
```

### Final Verification

```text
Status: PASS

Implementation Check: PASS
Integration Check: PASS

Remaining Issues:
No critical implementation issues.
```

The verifier can also identify limitations, such as missing automated tests, instead of silently ignoring them.

---

## 6. Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI / Agent Layer

* OpenAI Agents SDK
* Groq-hosted LLM
* Llama 3.1 8B Instant

### Agent Architecture

* Requirements Agent
* Codebase Analyst
* Development Planner
* Developer Agent
* Verification Agent

### Developer Tooling

* File discovery
* File reading
* File writing
* File updating
* Code search

### Environment

* Python virtual environment
* Environment variables for API configuration

---

## 7. Project Structure

```text
devflow-ai/
│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── agents/
│   │   ├── requirements.py
│   │   ├── codebase.py
│   │   ├── planner.py
│   │   ├── developer.py
│   │   └── verifier.py
│   │
│   ├── tools/
│   │   └── developer.py
│   │
│   └── model.py
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── models/
│   └── utils.py
│
├── docs/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> The exact application structure can vary depending on the project being modified. DevFlow AI is designed to analyze an existing codebase rather than require a fixed application architecture.

---

## 8. Developer Tools

DevFlow's developer tools provide controlled project manipulation.

### `list_files`

Lists files within the project while ignoring generated or dependency directories such as:

```text
.git
.venv
__pycache__
.pytest_cache
node_modules
```

### `read_file`

Reads UTF-8 project files.

### `write_file`

Creates a new file or completely replaces an existing file.

### `update_file`

Replaces a specific section of an existing file.

### `search_code`

Searches source and configuration files for a specific term and reports matching file locations and line numbers.

---

## 9. Safety

DevFlow's file operations are restricted to the project directory.

Before accessing a path, the tool resolves it and verifies that it remains inside the project root.

```text
Requested Path
      ↓
Resolve Path
      ↓
Check Project Root
      ↓
Allowed? ── No ──→ Access Denied
      │
     Yes
      ↓
Perform Operation
```

This helps prevent path traversal and accidental modification of files outside the project.

---

## 10. Installation

Clone the repository and create a virtual environment.

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the required model/API credentials in the environment.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Do not commit API keys to Git.

---

## 11. Running DevFlow AI

From the project root:

```powershell
python -m backend.main
```

DevFlow will display:

```text
============================================================
                    DEVFLOW AI
============================================================

Enter the feature/request you want to implement:
>
```

Enter a software development request.

Example:

```text
Add a health check endpoint to the FastAPI backend
that returns the application status and version.
```

DevFlow then executes the complete agent pipeline.

---

## 12. Output

A completed run produces a consolidated report containing:

```text
REQUIREMENTS ANALYSIS
        ↓
CODEBASE ANALYSIS
        ↓
DEVELOPMENT PLAN
        ↓
IMPLEMENTATION REPORT
        ↓
VERIFICATION REPORT
```

This gives the developer a complete record of what the AI understood, planned, changed, and verified.

---

## 13. Key Advantages

### Multi-Agent Separation

Each agent has a clearly defined responsibility instead of relying on one general-purpose prompt.

### Codebase Awareness

The system analyzes the actual project before making changes.

### Autonomous Implementation

The Developer Agent can directly modify project files using controlled tools.

### Independent Verification

A separate verification stage reviews the developer's work.

### Structured Development

Every request follows a repeatable engineering workflow.

### Extensibility

Additional agents can be added later for:

* Testing
* Security analysis
* Documentation
* Code review
* Dependency management
* Deployment
* Performance analysis

---

## 14. Current Limitations

The current version has a few known limitations:

* Automated test execution is not yet a mandatory part of verification.
* Some application-specific assumptions may require human review.
* Model token limits can affect very large codebases.
* The system depends on the configured LLM provider.
* Verification quality depends partly on the available codebase context.

These limitations provide clear opportunities for future development.

---

## 15. Future Scope

### Automated Testing Agent

Automatically generate and execute tests after implementation.

```text
Developer
    ↓
Testing Agent
    ↓
Test Results
    ↓
Verification Agent
```

### Security Agent

Scan modifications for:

* Authentication issues
* Secrets
* Injection vulnerabilities
* Unsafe file operations
* Dependency vulnerabilities

### Git Integration

Automatically:

* Create branches
* Commit changes
* Generate commit messages
* Create pull requests

### CI/CD Integration

Connect DevFlow to CI pipelines for automated development and verification.

### Multi-Model Routing

Use different models for different tasks.

```text
Planning → Reasoning Model
Coding → Code Model
Verification → Review Model
```

### Human Approval Gates

Allow developers to approve changes before they are written to the codebase.

---

## 16. Vision

DevFlow AI aims to move software development from:

```text
Prompt → Code
```

toward:

```text
Requirement
     ↓
Understand
     ↓
Analyze
     ↓
Plan
     ↓
Implement
     ↓
Verify
     ↓
Deliver
```

The long-term goal is an AI software engineering system that behaves less like a code generator and more like a **collaborative autonomous development team**.

---

## 17. Project Status

**Core multi-agent development pipeline: COMPLETE**

Current workflow:

```text
                    DEVFLOW AI

                       USER
                        │
                        ▼
               REQUIREMENTS AGENT
                        │
                        ▼
                CODEBASE ANALYST
                        │
                        ▼
                DEVELOPMENT PLANNER
                        │
                        ▼
                  DEVELOPER AGENT
                        │
                        ▼
                VERIFICATION AGENT
                        │
                        ▼
                 FINAL DEVFLOW RESULT
```

The system has been successfully demonstrated with a real FastAPI health-check feature request.

---

## 18. License

Add the project's chosen license here before publishing the repository.

---

## 19. Author

**Vidhaan Mathur**

DevFlow AI — Autonomous AI Software Development Workflow
