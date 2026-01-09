# Tests README

Hi team, Anvin here. This file explains our testing strategy for the Skyron project.

## Objective

As we build our project, we need to make sure that our code is reliable and that it's doing what we expect it to do. That's where testing comes in. By writing tests, we can:
- Catch bugs early.
- Make sure that our code is working as intended.
- Refactor our code with confidence.

## Implementation Plan

We'll use a combination of different types of tests to ensure the quality of our code:

### 1. Unit Tests

Unit tests are small, focused tests that test a single unit of code, such as a function or a class. We'll use the `pytest` framework for writing our unit tests.

Each module in the `src` directory should have its own corresponding test file in the `tests` directory. For example, the tests for `src/data_processing/pdf_extractor.py` will be in `tests/data_processing/test_pdf_extractor.py`.

### 2. Integration Tests

Integration tests are tests that test how different parts of our system work together. For example, we could write an integration test that:
- Extracts text from a PDF.
- Generates an embedding for the text.
- Stores the embedding in ChromaDB.
- Retrieves the embedding from ChromaDB.

Integration tests are more complex than unit tests, but they're essential for ensuring that our system is working as a whole.

## How to Contribute

- **Write tests for your code:** Whenever you write new code, please write tests for it.
- **Help improve our test coverage:** If you see a part of our codebase that isn't well-tested, please write some tests for it.

By writing tests, we can make our project more robust, more reliable, and easier to maintain.
