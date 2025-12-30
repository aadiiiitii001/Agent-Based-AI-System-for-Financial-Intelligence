def sanitize_input(text: str) -> str:
    """
    Prevents basic injection-style attacks.
    """
    return text.replace(";", "").replace("--", "")
