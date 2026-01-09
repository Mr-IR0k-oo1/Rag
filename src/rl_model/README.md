# Reinforcement Learning Model README

Hi team, Anvin here. This is where we'll be building the "brain" of our Skyron project. This document outlines our plan for implementing the reinforcement learning model.

## Objective

Our goal is to create a language model that is an expert in rocket science. We want it to be able to not only answer questions but also to generate new and innovative designs for rocket systems. To achieve this, we'll use a combination of supervised fine-tuning and reinforcement learning.

## Implementation Plan

### 1. Base Model Selection

We'll start with a pre-trained language model from the Hugging Face Hub. A good starting point would be a moderately sized model like `distilgpt2` or a small version of `Mistral`. These models are powerful enough to understand language, and they're small enough to be fine-tuned with reasonable computational resources.

### 2. Supervised Fine-tuning (SFT)

Before we can use reinforcement learning, we need to adapt our base model to the domain of rocket science. We'll do this with supervised fine-tuning.

1.  **Dataset Creation:** We'll create a dataset of question-answer pairs from our books. This will be a crucial step, as the quality of our dataset will directly impact the performance of our model. We can use a pre-trained QA model to help us with this, or we can create the dataset manually.
2.  **Fine-tuning:** We'll use TRL's `SFTTrainer` to fine-tune our base model on the question-answering dataset. This will teach the model the language of rocketry and improve its ability to answer questions on the topic.

### 3. Reinforcement Learning with Human Feedback (RLHF)

This is the most exciting and challenging part of the project. We'll use reinforcement learning to teach our model to be creative and generate new designs.

1.  **Reward Model:** We'll need to create a "reward model" that can score the quality of our model's generated output. This is a complex task, as there's no single "right" answer when it comes to design. We can start with a simple reward model based on heuristics, and then we can improve it over time. For example, we could reward the model for generating designs that are:
    *   **Physically plausible:** Do they obey the laws of physics?
    *   **Performant:** Do they have a high delta-v, payload capacity, or specific impulse?
    *   **Novel:** Are they new and interesting?
2.  **RL Fine-tuning:** We'll use TRL's `PPOTrainer` to fine-tune our SFT model using the reward model. This will train the model to generate outputs that maximize the reward, leading to better and more innovative rocket designs.

## How to Contribute

- **Help with dataset creation:** This is a huge task, and any help would be appreciated.
- **Develop the reward model:** This is a great opportunity to get creative and think about what makes a "good" rocket design.
- **Experiment with different RL algorithms:** TRL supports different RL algorithms. We can experiment with them to see which one works best for our project.

This is the most ambitious part of our project, but it's also the most exciting. Let's build an AI that can help us push the boundaries of rocket science!
