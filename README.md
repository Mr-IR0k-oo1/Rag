# Skyron RAG Project

Hi everyone, Anvin here! I'm excited to share the vision and plan for our Skyron RAG project. This document will serve as our guide as we build this innovative system together.

## Project Overview

The goal of the Skyron project is to create a Reinforcement Learning (RL) based RAG (Retrieval-Augmented Generation) system. Think of it as an AI that can read and understand a whole library of books on rocket science and then use that knowledge to design new and better rocket systems. We're not just building a question-answering bot; we're building a creative AI that can learn and innovate.

## Architecture

Our system will have a few key components:

- **Data Ingestion Pipeline:** This is where we'll feed the AI its "textbooks." We'll have scripts to process PDFs, extract the text, and prepare it for the model.
- **Vector Database:** We'll use ChromaDB to store the "memories" of the AI. These memories will be in the form of embeddings, which are numerical representations of the text.
- **Language Model (LLM):** The "brain" of our operation. We'll start with a pre-trained LLM and then fine-tune it to become an expert in rocketry.
- **Reinforcement Learning Agent:** This is the "teacher" that will guide the LLM to generate better and more creative designs. It will provide feedback to the LLM based on a reward function.
- **Application Interface:** A simple way for us to interact with our creation, ask it questions, and see what it comes up with.

## Development Roadmap

We'll build this project in phases. Here's the plan:

### Phase 1: Data Ingestion and Processing

This is the foundation of our project. We need to get the data into a format that our AI can understand.
**For more details, see the [Data Processing README](src/data_processing/README.md).**

### Phase 2: Initial Model Fine-tuning (Supervised)

Once we have our data, we'll start training our AI. We'll begin with supervised fine-tuning to teach the model the basics of rocket science.
**For more details, see the [RL Model README](src/rl_model/README.md).**

### Phase 3: Reinforcement Learning Fine-tuning (RLHF)

This is where the magic happens. We'll use reinforcement learning to teach our AI to be creative and generate new designs.
**For more details, see the [RL Model README](src/rl_model/README.md).**

### Phase 4: Application Development

Finally, we'll build an interface to interact with our AI.

## Getting Started

1.  Clone the repository:
    ```bash
    git clone https://github.com/Mr-IR0k-oo1/Rag.git
    cd Rag
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Contribute

I'm excited to have you on board! If you have ideas, suggestions, or want to contribute to the code, please feel free to open an issue or submit a pull request. Let's build something amazing together!

---

*This `README.md` is a living document. I'll be updating it as we make progress, and I encourage you to do the same.*
