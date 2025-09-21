import random

def simplify_legal_text(text: str) -> str:
    """
    Mock AI function to simplify legal text.
    It generates a "simplified" version with random phrasing.
    """
    # Example mock simplifications
    simplifications = [
        "In simple terms: ",
        "Basically, this means: ",
        "What it really says is: ",
        "In plain language: ",
        "To put it simply: "
    ]
    
    # Split text into sentences (roughly)
    sentences = text.split(".")
    simplified_sentences = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            simplified = random.choice(simplifications) + sentence.lower()
            simplified_sentences.append(simplified)
    
    return " ".join(simplified_sentences)
