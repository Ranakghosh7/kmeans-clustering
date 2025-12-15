# Bias-Aware Automated Feedback System for Student Writing

##  Limitations, Reproducibility, and Research Positioning

This section situates the project as a **research-style mini study**, clarifies its limitations, and explains how it can be reproduced and evaluated by others. This is a critical section for research programs (such as Caltech SURF) because it demonstrates scientific maturity, not just implementation skills.

---

### A. System Limitations

Despite promising qualitative results, this project has several important limitations:

1. **Model Dependence**
   The bias detection component relies on a locally hosted large language model (LLaMA 3 via Ollama). While this enables free, offline experimentation, it introduces variability in outputs depending on model version, prompt phrasing, and inference temperature.

2. **Non-deterministic Outputs**
   Since large language models are generative, identical inputs may yield slightly different outputs across runs. This limits strict reproducibility of exact results, although trends and qualitative behaviors remain consistent.

3. **Synthetic Evaluation Data**
   Many bias tests rely on synthetically modified text (e.g., demographic swap tests). While this is common in fairness research, it may not fully capture real-world linguistic complexity.

4. **Lack of Human Evaluation**
   This project does not include large-scale human annotation or expert evaluation of feedback quality. Results are therefore primarily machine- and prompt-based.

5. **Resource Constraints**
   The project was intentionally designed to run on consumer-grade hardware (4–8GB VRAM). As a result, model size and inference depth are limited compared to cloud-based systems.

---

### B. Reproducibility Strategy

Although full determinism is not guaranteed, the project emphasizes **procedural reproducibility**, meaning that another researcher can follow the same steps and reach comparable conclusions.

Reproducibility is ensured through:

* Open-source code hosted on GitHub
* Explicit dependency listing (`requirements.txt`)
* Clear directory structure (`src/`, `paper/`, `results/`)
* Prompt templates embedded directly in the source code
* Local inference via Ollama (no API keys required)

To reproduce the experiments:

1. Install Ollama and download the LLaMA 3 model
2. Clone the GitHub repository
3. Run the bias detection module on provided sample texts
4. Observe qualitative differences across biased vs neutral inputs

---

### C.  Research Ethics and Safety Considerations

Bias analysis inherently involves sensitive topics such as gender, race, and socioeconomic status. To mitigate harm:

* No personal data is used
* All test sentences are synthetic or anonymized
* Outputs are framed as **analytical observations**, not judgments
* The system avoids reinforcing stereotypes by explicitly labeling detected bias

This aligns with responsible AI research practices.

---

### D.  Intended Contributions

Although small in scale, this project contributes the following:

* A **fully local, free bias analysis pipeline** using modern LLMs
* A practical demonstration of fairness-aware NLP principles
* A reproducible template for student-led AI ethics research
* A bridge between theory (bias/fairness) and deployment (local inference)

---

### E.  Positioning as a Research Mini-Project

This work is intentionally framed as a **research-style mini project**, not a production system. Its value lies in:

* Clear research motivation
* Explicit assumptions and limitations
* Structured experimentation
* Ethical awareness
* Transparent reporting

These qualities are central to undergraduate research programs and academic evaluation.

---

### F. Future Work

Several extensions are possible:

* Quantitative benchmarking with labeled bias datasets
* Human evaluation studies
* Prompt optimization experiments
* Cross-model comparisons
* Integration with educational writing tools

---

**Summary:**
This section demonstrates that the project is not only functional but also *scientifically reasoned*, ethically grounded, and reproducible—key qualities of credible research.
