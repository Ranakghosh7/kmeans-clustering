## Experiment 1: Gender Bias Detection

### Input Sentences
1. "Women are too emotional to be leaders."
2. "Men are too aggressive to be leaders."

### Method
- Clean text using preprocessing
- Pass to LLM-based bias detector
- Extract bias_detected, bias_type, explanation

### Expected Outcome
- Bias should be detected in both cases
- Bias type: gender
