# preprocess.py
import re
import emoji
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)
STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove emojis
    text = emoji.replace_emoji(text, replace="")

    # Lowercase
    text = text.lower()

    # Remove punctuation/symbols
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Remove stopwords
    words = [w for w in text.split() if w not in STOPWORDS]
    return " ".join(words)

if __name__ == "__main__":
    sample = "This is a TEST 😊 with a URL: https://example.com and Emojis!"
    print(clean_text(sample))
