import sys
import os
import json
import subprocess  
# Add the project root path so Python can find preprocess.py
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from preprocess import clean_text


def query_ollama(prompt: str, model: str = "llama3"):
    """
    Sends a prompt to Ollama and returns the text output.
    Requires: `ollama run llama3` to be available.
    """

    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    out, err = process.communicate(prompt)

    if err:
        print("Ollama error:", err)

    return out.strip()


def detect_bias(text: str):
    """
    Detects bias in text using Llama3 through Ollama.
    Returns a structured JSON-like dictionary.
    """

    cleaned = clean_text(text)

    system_prompt = f"""
You are a precise text bias classifier. Analyze the following text
and return ONLY a JSON object with these fields:

- bias_detected: true/false
- bias_type: short string (e.g. gender, race, age, religion, political, socioeconomic, none)
- explanation: brief explanation in one sentence

Text to analyze: "{cleaned}"
"""

    result = query_ollama(system_prompt)

    # Try parsing JSON
    try:
        parsed = json.loads(result)
    except:
        # If there is extra text, extract only the JSON part
        try:
            json_part = result[result.index("{"): result.rindex("}") + 1]
            parsed = json.loads(json_part)
        except:
            parsed = {
                "bias_detected": False,
                "bias_type": "unknown",
                "explanation": "LLM returned unexpected output."
            }

    return parsed


if __name__ == "__main__":
    sample = "Women are too emotional to be leaders."
    output = detect_bias(sample)
    print(json.dumps(output, indent=2))
