"""
Presidio Analyzer — public docs examples (MIT).
Sources:
  https://raw.githubusercontent.com/microsoft/presidio/main/docs/analyzer/index.md
  https://raw.githubusercontent.com/microsoft/presidio/main/docs/analyzer/adding_recognizers.md
Fetched: 2026-09-19. Study only — requires `pip install presidio-analyzer` (+ spaCy model) to run.
"""

# --- Hello analyze (docs) ---
from presidio_analyzer import AnalyzerEngine

analyzer = AnalyzerEngine()
results = analyzer.analyze(
    text="My phone number is 212-555-5555",
    entities=["PHONE_NUMBER"],
    language="en",
)
print(results)

# --- PatternRecognizer / deny-list (docs) ---
from presidio_analyzer import PatternRecognizer, AnalyzerEngine, RecognizerRegistry

titles_recognizer = PatternRecognizer(
    supported_entity="TITLE",
    deny_list=["Mr.", "Mrs.", "Miss"],
)

registry = RecognizerRegistry()
registry.load_predefined_recognizers()
registry.add_recognizer(titles_recognizer)
analyzer = AnalyzerEngine(registry=registry)
print(analyzer.analyze(text="His name is Mr. Jones", language="en"))

# --- Ad-hoc regex idea (API JSON shape from docs) ---
# Useful for plant-specific secret patterns without forking Presidio:
AD_HOC_REGEX_SHAPE = {
    "name": "Zip code Recognizer",
    "supported_language": "en",
    "patterns": [
        {"name": "zip code (weak)", "regex": r"(\b\d{5}(?:\-\d{4})?\b)", "score": 0.01}
    ],
    "context": ["zip", "code"],
    "supported_entity": "ZIP",
}
