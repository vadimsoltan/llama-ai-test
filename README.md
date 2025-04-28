# llama-ai-test

## Overview

`llama-ai-test` is a FastAPI application implementing Retrieval-Augmented Generation (RAG) using the `llama-index` framework.

## Requirements

- [Poetry](https://python-poetry.org/) for dependency management.

## Setup

1. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

2. Create the required directories:

   ```bash
   mkdir -p data storage
   ```

## Usage

Run the application with:

```bash
poetry run python3 -m app
```

Note: The vector index is rebuilt on every application startup.