# Data Processing README

Hi team, Anvin here. This document outlines our plan for the data processing phase of the Skyron project. This is a critical first step, as the quality of our data will directly impact the performance of our AI model.

## Objective

The goal of this phase is to take the raw PDF documents in the `data/raw_pdfs` directory and transform them into a clean, structured dataset that we can use for training our language model.

## Implementation Plan

Here's how we'll approach this:

### 1. PDF Text Extraction

Our first step is to get the text out of the PDF files. We'll use the `pypdf` library for this, as it's already included in our `requirements.txt`.

The script `pdf_extractor.py` will be our starting point. It will:
- Iterate through all the PDF files in the `data/raw_pdfs` directory.
- For each PDF, extract the text from every page.
- Save the extracted text to a new file in the `data/extracted_text` directory.

**A note on challenges:** Some PDFs, especially scanned documents, might be difficult to process. We may need to incorporate Optical Character Recognition (OCR) tools like `pytesseract` if we find that `pypdf` is not sufficient for all the documents.

### 2. Text Chunking

Once we have the raw text, we need to break it down into smaller, more manageable chunks. This is important for two reasons:
- **Embedding:** Most embedding models have a limit on the number of tokens they can process at once.
- **Retrieval:** Smaller chunks allow for more granular retrieval of information.

We'll need to develop a "smart" chunking strategy. Instead of just splitting the text by a fixed number of characters, we'll aim to split it by sections, paragraphs, or other logical divisions. This will help to preserve the context of the information.

### 3. Embedding Model Selection

We'll use a pre-trained sentence transformer model from the Hugging Face Hub to generate our embeddings. A good starting point would be the `all-MiniLM-L6-v2` model, as it offers a good balance between performance and computational cost.

### 4. Embedding Generation and Storage

Once we have our text chunks, we'll create a script to:
- Load the pre-trained embedding model.
- Generate an embedding for each text chunk.
- Store the embeddings, along with the original text and any relevant metadata (e.g., the source document), in our ChromaDB vector database.
**For more details on the ChromaDB setup, see the [ChromaDB README](src/chroma_db/README.md).**

## How to Contribute

If you're interested in helping with this phase, here are a few things you can do:
- **Improve `pdf_extractor.py`:** Can we make it more robust? Can we add better error handling?
- **Develop a text chunking strategy:** Research and implement a smart chunking strategy.
- **Experiment with embedding models:** Try out different embedding models and see how they perform.

Let's get this data ready for our AI!
