# NOTES — Presidio Analyzer (PII / secrets)

**Intent:** G9 secret/PII gate patterns. Regex first; Presidio optional via pip.

## Analyzer model

```text
AnalyzerEngine
  ├── RecognizerRegistry  (predefined + custom EntityRecognizers)
  ├── NlpEngine           (spaCy / stanza / transformers — optional weight)
  └── ContextAwareEnhancer
         ↓
   List[RecognizerResult]  {entity_type, score, start, end}
```

Docs: https://github.com/microsoft/presidio/blob/main/docs/analyzer/index.md

## Recognizer families (for our gate)

| Type | Use for KWB |
|---|---|
| Deny list | Titles / known plant codenames (careful with false positives) |
| Pattern / regex | API keys, tokens, account-ish strings (overlap our existing regex gate) |
| NER / ML | Names, locations — heavier; optional later offline |
| RemoteRecognizer | **Refuse** for air-gap (external HTTP detector) |

## Honesty constraint

Presidio project itself warns detection is incomplete. Our freezes: **regex + optional Presidio**; never claim full DLP.

## Bind points

- Before Word/export (G9).
- Before audit JSONL if logging model output (redact).
- Do not scan GPU weights or train.

## Prefer

`pip install presidio-analyzer` at runtime when deepening — do not vendor the monorepo.
