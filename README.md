# README for llama-ai-test

## Project Overview

`llama-ai-test` is a FastAPI application that implements the Retrieval-Augmented Generation (RAG) approach using the `llama-index` framework. This project aims to provide a robust API for generating responses based on retrieved information, enhancing the capabilities of traditional language models.

## Features

- FastAPI framework for building APIs
- Integration with `llama-index` for RAG

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd llama-ai-test
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -e .
   ```

## Usage

To run the FastAPI application, execute the following command:

```bash
uvicorn app.main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

The application provides several endpoints for interacting with the RAG service. Refer to the API documentation for detailed information on available endpoints and their usage.

## Testing

To run the tests, use the following command:

```bash
pytest
```

This will execute all unit tests defined in the `tests` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.