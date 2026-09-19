# GPU and Model Choices

## Prototype tier

- 16–24 GB VRAM: workable for 7B–14B quantised models
- 32–48 GB VRAM: more comfortable for 14B–32B quantised models
- CPU inference is possible but slow
- Single NVIDIA RTX 4090/5090-class GPU or workstation GPU is suitable for experimentation
- Use local embeddings and reranking models

## Pilot tier

- 48–80 GB VRAM preferred
- One or more data-centre GPUs (NVIDIA L40S, A100 or H100-class)
- 128–256 GB system RAM
- Fast NVMe storage for OCR, indexes and document previews
- Separate storage for raw documents, embeddings, logs and generated artefacts

## Production tier

Production depends on:

- Number of users
- Context length
- Concurrent requests
- OCR volume
- Model size
- Need for multiple models
- Fine-tuning
- Historian analytics
- High availability

Realistic architecture:

- Small model for classification, extraction and routing
- Medium model for standard reports and RAG
- Larger model for complex analysis
- Separate vision/OCR model
- Separate embedding and reranking models
- Optional time-series/anomaly models

## Model strategy

Do not promise that one model will do everything. Use:

- A fast 7B–14B model for extraction and workflow routing
- A 14B–32B model for technical drafting and comparison
- A larger model only for difficult reasoning or batch processing
- A vision-language model for diagrams, tables and scanned reports
- Deterministic Python/SQL calculators for engineering and finance

## Model selection criteria

Model choice should be driven by:

- Licence
- Offline availability
- Indian-language support
- Context length
- Quantisation quality
- Hardware demand
- Hallucination behaviour
- Security review
- Domain evaluation

## Multi-model routing

Task classification determines model:

| Task type | Model role |
|---|---|
| Document classification | Small router model |
| OCR post-processing | Fast extraction model |
| Table extraction | Vision-language model |
| Technical reasoning | Larger reasoning model |
| Calculation | Python sandbox |
| Document generation | Medium generation model |
| Embedding | Embedding model |
| Reranking | Cross-encoder |

## Organisation-level architecture (production)

| Layer | Organisation-level specification |
|---|---|
| GPU compute | 4–8× NVIDIA H100 or L40S in dedicated inference cluster |
| CPU compute | 64–128 cores across application servers |
| RAM | 512 GB–1 TB per node |
| Storage | NVMe SSD for hot data; HDD/SAN for cold data |
| Network | 10–100 Gbps internal; isolated VLANs for OT, IT, and AI enclaves; no external connectivity |
| Backup | Offline/air-gapped backup with encrypted media |
| Power | UPS + captive power/generator backup |
| Physical security | Restricted-access data centre; biometric entry; CCTV; no removable media |
