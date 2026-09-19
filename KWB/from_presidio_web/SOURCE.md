# SOURCE — from_presidio_web

**Upstream:** [microsoft/presidio](https://github.com/microsoft/presidio) (also mirrored at data-privacy-stack/presidio)  
**Fetched:** 2026-09-19 (web docs + raw)  
**License:** MIT  
**Role:** PII/secret detection patterns for G9 (optional `pip install presidio-analyzer`; we already have regex secrets gate).

## URLs used

| What | URL |
|---|---|
| Analyzer docs | https://raw.githubusercontent.com/microsoft/presidio/main/docs/analyzer/index.md |
| Adding recognizers | https://raw.githubusercontent.com/microsoft/presidio/main/docs/analyzer/adding_recognizers.md |
| Analyzer package tree | https://github.com/microsoft/presidio/tree/main/presidio-analyzer |
| LICENSE | https://raw.githubusercontent.com/microsoft/presidio/main/LICENSE |
| PyPI | https://pypi.org/project/presidio-analyzer/ |

## What KWB will use later

- Optional `AnalyzerEngine.analyze(...)` behind export / DRAFT gates.
- `PatternRecognizer` / deny-list / regex for plant-specific secret shapes.
- Keep regex gate on critical path; Presidio is **optional deepen** (TECH_STACK_VERIFY).

## Refuse list

- Cloud Azure Text Analytics / AHDS as required detector.
- LangExtract + cloud LLM PII path for air-gap demo.
- Full Presidio stack (image redactor, structured) as must-ship.
- Treating Presidio as complete DLP (upstream warns incomplete detection).

## Files

| File | Kind |
|---|---|
| `SOURCE.md` | this |
| `NOTES.md` | study |
| `excerpt_analyzer_hello.py` | docs hello + PatternRecognizer |
| `LICENSE.MIT.txt` | notice |
