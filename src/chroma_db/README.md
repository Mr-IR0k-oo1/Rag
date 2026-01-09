# ChromaDB README

Hi everyone, Anvin here. This file explains how we'll use ChromaDB in our Skyron project.

## Objective

ChromaDB will be our vector database. It will store the embeddings of the text chunks we extract from the books, and it will allow us to perform efficient similarity searches to find the most relevant information for a given query.

## Implementation Plan

### 1. Setting up ChromaDB

We'll use the `chromadb` Python library, which is already included in our `requirements.txt`. We will start with an in-memory database for simplicity, and we can later move to a persistent database if needed.

We will create a dedicated module in this directory, for example `chroma_utils.py`, to handle all interactions with ChromaDB. This module will include functions for:
- Initializing the ChromaDB client.
- Creating a new collection for our embeddings.
- Adding embeddings to the collection.
- Querying the collection for similar embeddings.

### 2. Creating a Collection

We'll create a single collection to store all our embeddings. We'll need to decide on a name for the collection (e.g., "skyron_rag").

### 3. Adding Embeddings

As we process the text chunks and generate embeddings in the data processing phase, we'll add them to our ChromaDB collection. Each entry in the collection will consist of:
- **An embedding:** The numerical representation of the text chunk.
- **A document:** The original text chunk.
- **Metadata:** A dictionary of metadata, such as the source document, page number, and any other relevant information.

### 4. Querying for Similar Embeddings

Once we have our embeddings stored in ChromaDB, we'll be able to query the database to find the most relevant text chunks for a given query. We'll do this by:
- Generating an embedding for the query.
- Using the `query` method of the ChromaDB collection to find the `n` most similar embeddings.

This will be a crucial part of our RAG (Retrieval-Augmented Generation) system, as it will allow us to retrieve the most relevant information from our knowledge base and provide it to the language model as context.

## How to Contribute

- **Develop `chroma_utils.py`:** Create the initial version of the module with the functions described above.
- **Research advanced ChromaDB features:** Explore features like filtering and collection management to see how we can use them to our advantage.
- **Optimize for performance:** As our dataset grows, we may need to optimize our ChromaDB setup for performance.

Let's build a powerful memory for our AI!
