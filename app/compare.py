import difflib

def diff_text(original: str, optimized: str):
    diff = difflib.ndiff(original.splitlines(), optimized.splitlines())
    return "\n".join(diff)
