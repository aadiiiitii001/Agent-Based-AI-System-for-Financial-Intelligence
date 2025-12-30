def extract_keywords(text: str):
    """
    Lightweight keyword extractor.
    Replace with NLP pipeline later.
    """
    keywords = []
    for word in ["risk", "compliance", "regulatory", "volatility"]:
        if word in text.lower():
            keywords.append(word)
    return keywords
