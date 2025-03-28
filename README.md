# SH RAG Chat

[![Release](https://img.shields.io/github/v/release/DCC-BS/rag-application)](https://img.shields.io/github/v/release/DCC-BS/rag-application)
[![Build status](https://img.shields.io/github/actions/workflow/status/DCC-BS/rag-application/main.yml?branch=main)](https://github.com/DCC-BS/rag-application/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/DCC-BS/rag-application/branch/main/graph/badge.svg)](https://codecov.io/gh/DCC-BS/rag-application)
[![Commit activity](https://img.shields.io/github/commit-activity/m/DCC-BS/rag-application)](https://img.shields.io/github/commit-activity/m/DCC-BS/rag-application)
[![License](https://img.shields.io/github/license/DCC-BS/rag-application)](https://img.shields.io/github/license/DCC-BS/rag-application)

This is a template repository for Python projects that use uv for their dependency management.

- **Github repository**: <https://github.com/DCC-BS/rag-application/>
- **Documentation** <https://DCC-BS.github.io/rag-application/>

## Getting started with your project

#### Pre-requisites

Windows
- Install [Git for Windows](https://git-scm.com/downloads/win)
- Install [Scoop](https://scoop.sh/)
- Install make: `scoop install make`

General
- Install [VSCode](https://code.visualstudio.com/)
- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:DCC-BS/rag-application.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).


# SH-RAG-Chat

A Python-based RAG (Retrieval-Augmented Generation) chat application with FastAPI backend and authentication support.

## Project Overview

This project implements a chat application with RAG capabilities, using LanceDB for vector storage and FastAPI for the backend API. The application includes user authentication, CLI tools, and a modern UI interface.

## Project Structure

```
sh-rag-chat/
├── src/                      # Source code
│   └── rag/                  # Main application package
│       ├── cli/              # Command-line interface tools
│       │   └── create_user.py  # User creation script
│       ├── conf/             # Configuration files
│       ├── core/             # Core RAG functionality
│       │   ├── rag_pipeline.py  # RAG pipeline implementation
│       │   ├── bento_embeddings.py  # Embedding models
│       │   ├── lance_retriever.py  # LanceDB retriever
│       │   └── rag_states.py  # State management
│       ├── data/             # Application data
│       ├── logs/             # Log files
│       ├── stubs/            # Type stubs
│       ├── ui/               # User interface
│       │   ├── app.py        # Streamlit application
│       │   ├── components/   # UI components
│       │   └── constants.py  # UI constants
│       ├── utils/            # Utility functions
│       ├── auth.py           # Authentication logic
│       ├── main.py           # FastAPI application entry point
│       ├── models.py         # Database models
│       └── setup_lancedb.py  # Vector DB setup
├── data/                     # External data files
│   ├── EL/                   # EL dataset
│   ├── EL2/                  # EL2 dataset
│   ├── SH/                   # SH dataset
│   └── dev/                  # Development data
├── lancedb/                  # LanceDB storage
│   └── documents.lance/      # Vector document storage
├── tests/                    # Test suite
├── docs/                     # Documentation
├── .venv/                    # Virtual environment (generated)
└── various config files      # (.gitignore, pyproject.toml, etc.)
```

## Langchain Graph

![Langchain Graph](graph.png)

## Features

- User Authentication and Authorization
- RAG-based Chat Interface
- Vector Storage with LanceDB
- FastAPI Backend
- CLI Tools for User Management
- Modern UI Components
- Comprehensive Testing Suite

## Technical Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite (via SQLModel)
- **Vector Storage**: LanceDB
- **Authentication**: JWT-based
- **Development Tools**:
  - UV (Package Manager)
  - Ruff (Linter)
  - Pyright (Type Checker)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sh-rag-chat.git
cd sh-rag-chat
```

2. Set up the Python environment:
```bash
# Using UV package manager
uv venv
source .venv/bin/activate  # On Unix
# or
.venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Configuration

1. Database Setup:
   - The application uses SQLite by default
   - Database configuration is in `api/models.py`
   - Run migrations using the CLI tools

2. Environment Variables:
   - Copy `.env.example` to `.env`
   - Configure necessary environment variables

## Usage

1. Start the API server:
```bash
# Unix
./api/run.sh

# Windows
./api/run.ps1
```

2. Create a new user:
```bash
python api/cli/create_user.py --username <username> --password <password> --organization <org>
```

3. Access the application:
   - API documentation: http://localhost:8000/docs
   - UI interface: http://localhost:8000

## Development

1. Code Style:
   - Follow PEP 8 guidelines
   - Use type hints
   - Run linter: `ruff check .`
   - Run type checker: `pyright`

2. Testing:
   - Run tests: `pytest api/tests/`
   - Coverage report: `pytest --cov=api`

## API Documentation

The API documentation is available at `/docs` when the server is running. Key endpoints include:

- `/auth/token` - Get authentication token
- `/chat` - Chat endpoint
- `/users` - User management
