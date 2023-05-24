# Demonstrate Usage of some basic Regular Expressions in Python

import re

# Example string
text = "The quick brown fox jumps over the lazy dog."

# Regular expression patterns
patterns = [
    r"fox",                      # Matches "fox"
    r"\b\w{5}\b",                # Matches words with exactly 5 characters
    r"\b[a-z]{3}\b",             # Matches lowercase words with exactly 3 characters
    r"[A-Z][a-z]+",              # Matches capitalized words
    r"\b[a-zA-Z]+\b",            # Matches any word
    r"\b[a-zA-Z]{4,}\b",         # Matches words with 4 or more characters
    r"\b[a-zA-Z]+s\b",           # Matches words ending with 's'
    r"\b[a-zA-Z]{3}s\b",         # Matches words with 3 characters ending with 's'
    r"\b[a-zA-Z]{4,}s\b"         # Matches words with 4 or more characters ending with 's'
]

# Perform regex matching and print the results
for pattern in patterns:
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print("Matches:", matches)
    print()
