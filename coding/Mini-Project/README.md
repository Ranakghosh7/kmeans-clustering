# Bias-Aware Automated Feedback System for Student Writing

## 📌 Project Overview

This repository contains a research-oriented NLP project designed to generate high-quality writing feedback **while detecting and mitigating potential linguistic or demographic biases**. The project is structured like an academic study to strengthen research experience for programs such as **Caltech SURF**.

---

## 🎯 Objectives

* Build a baseline automatic writing feedback generator.
* Detect bias using sentiment shifts, toxicity scoring, and demographic swap tests.
* Implement mitigation strategies to reduce unfair or biased behaviors.
* Compare baseline vs. bias-aware feedback systems.
* Present results through experiments, analysis, and visualizations.

---

## 🧠 Research Questions

1. Can an LLM provide useful feedback while actively monitoring for bias?
2. Does a structured bias mitigation pipeline improve fairness?
3. Do mitigation strategies affect feedback quality?

---

## 📂 Repository Structure

```
bias-aware-feedback-nlp/
│── README.md
│── data/
│   ├── raw_samples/
│   ├── bias_test_pairs/
│── src/
│   ├── generator.py
│   ├── bias_detector.py
│   ├── mitigation.py
│   ├── evaluation.py
│   ├── utils.py
│── notebooks/
│   ├── baseline_experiments.ipynb
│   ├── bias_tests.ipynb
│   └── mitigation_ablation.ipynb
│── results/
│   ├── plots/
│   └── metrics/
│── demo/
│   └── app.py
│── paper/
│   └── mini_research_report.pdf
```

---

## 🔧 Methodology Overview

### 1. Data Collection

* Collect public writing samples.
* Create paired samples with demographic swaps.

### 2. Baseline Feedback Generator

* LLM-based writing feedback.
* Raw, no mitigation.

### 3. Bias Detection Module

* Sentiment analysis
* Toxicity classification
* Politeness scoring
* Demographic swap consistency checks

### 4. Bias Mitigation

* Prompt constraints
* Re-ranking
* Filtering strategies

### 5. Evaluation

* Quality metrics
* Fairness metrics
* Explainability outputs

---

## 📊 Planned Experiments

### **Experiment 1 — Baseline vs Bias-Aware System**

Compare suggestion quality and fairness.

### **Experiment 2 — Swap-Test Evaluation**

Measure sentiment and style shifts across demographic variants.

### **Experiment 3 — Ablation Study**

Evaluate which mitigation components contribute most to fairness.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* PyTorch
* HuggingFace Transformers
* SpaCy
* FairLearn / AIF360
* Streamlit

### Installation

```
git clone https://github.com/Ranakghosh7/bias-aware-feedback-nlp.git
cd bias-aware-feedback-nlp
pip install -r requirements.txt
```

### Run Streamlit Demo

```
streamlit run demo/app.py
```

---

## 📝 To-Do

* [ ] Add initial dataset samples
* [ ] Implement baseline generator
* [ ] Build bias detection module
* [ ] Add mitigation strategies
* [ ] Conduct experiments
* [ ] Add results and plots
* [ ] Write full research paper

---

## 📄 License

MIT License

---

## ✨ Author

This project was created as part of a research portfolio for competitive undergraduate research opportunities.
