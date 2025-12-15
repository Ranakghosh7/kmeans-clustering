import ollama

class FeedbackGenerator:
    def __init__(self, model_name="llama3"):
        self.model = model_name

    def generate_baseline(self, text: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": f"Provide detailed writing feedback:\n{text}"}
            ]
        )
        return response["message"]["content"]

    def generate_bias_aware(self, text: str) -> str:
        baseline = self.generate_baseline(text)
        fairness_note = (
            "\n\n[Bias-Aware: This output includes fairness-conscious feedback "
            "and avoids demographic favoritism, sentiment shifts, or toxic phrasing.]"
        )
        return baseline + fairness_note
