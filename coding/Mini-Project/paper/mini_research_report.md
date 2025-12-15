# Bias Detection in Text Using Local Large Language Models

## Abstract
This mini research project investigates the feasibility of detecting
social and linguistic bias in text using locally deployed large language
models (LLMs). Unlike cloud-based APIs, this system relies on an offline
deployment of LLaMA-3 via Ollama, emphasizing reproducibility, privacy,
and accessibility. The project explores prompt-based bias classification,
system architecture, and deployment challenges in real-world environments.

## 1. Introduction
Bias in language models and automated text systems has become a growing
concern in educational, social, and professional settings. Automated
bias detection can help identify harmful stereotypes and unfair language.
This project aims to explore whether locally deployed LLMs can be used
as lightweight bias detectors without relying on external APIs.

## 2. Related Work
Prior work in bias detection typically relies on:
- Supervised classifiers
- Lexicon-based methods
- Cloud-hosted LLM APIs

This project differs by focusing on:
- Fully local inference
- Prompt-based classification
- System-level experimentation

## 3. System Architecture
The system consists of three main components:

1. Text preprocessing module
2. Bias detection module using prompt engineering
3. Local LLM inference using Ollama (LLaMA-3)

The architecture prioritizes modularity and transparency.

## 4. Methodology
Bias detection is performed by prompting the LLM to return a structured
JSON object containing:
- bias_detected
- bias_type
- explanation

This approach avoids explicit training and instead evaluates the
zero-shot reasoning ability of the model.

## 5. Experiments
Experiments were conducted on manually selected sentences containing
potential gender, racial, and social bias.

Example input:
"Women are too emotional to be leaders."

Expected output format:
```json
{
  "bias_detected": true,
  "bias_type": "gender",
  "explanation": "The statement reinforces a gender stereotype."
}
