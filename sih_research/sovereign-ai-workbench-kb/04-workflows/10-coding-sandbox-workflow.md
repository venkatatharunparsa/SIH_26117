# Coding and Sandbox Workflow

The SIH problem statement explicitly requires: "A coding task run and verified in a sandbox." This file documents that workflow.

## Why coding matters

The workbench must generate and execute code for tasks that need deterministic, reproducible results:

- Corrosion-rate calculations from extracted thickness readings
- Material and energy balances
- Yield and mass-balance reconciliation
- Cost variance calculations
- Reliability statistics
- Data cleaning and merging across historian, LIMS and EAM exports
- Ad-hoc analysis scripts for one-off investigations
- Internal tool scripts requested by users

The language model writes the code. The sandbox executes it. The engineer validates the output.

## Workflow

1. User asks a question that requires calculation or data processing
2. Router classifies the request as a coding task
3. A code-specialised model generates Python (or R) code
4. Code is statically checked (imports, lint, obvious errors)
5. Code is executed in an isolated sandbox with:
   - No network access
   - Read-only access to whitelisted data files
   - Write access only to a temporary working directory
   - CPU and memory limits
   - Execution time limit
   - No access to host system or other users
6. Output (stdout, generated files, charts) is captured
7. Results are attached to the response with the code shown for review
8. Engineer reviews both the code and the result
9. If accepted, the result becomes part of the document or calculation record

## Sandbox options

| Option | Isolation | Air-gap compatible | Notes |
|---|---|---|---|
| Docker | Container | Yes | Widely used; needs daemon |
| Podman | Container, rootless | Yes | Rootless, good for shared hosts |
| Firejail | Process | Yes | Lightweight on Linux |
| nsjail | Process | Yes | Google; strong isolation |
| gVisor | Kernel | Yes | Strong syscall isolation |
| bubblewrap | Process | Yes | Used by Flatpak |
| Pyodide / WASM | In-process | Yes | Limited libraries; no filesystem |
| E2B / cloud sandbox | Container | No | Not air-gap compatible |

For an air-gapped deployment, use Docker or Podman with a deny-all network policy, read-only bind mounts, and resource limits.

## Demo coding task

For the 36-hour hackathon demo, a strong coding task is:

**User prompt:** "Extract the thickness readings from this scanned inspection report, match them to the historical readings in the equipment history, calculate the long-term and short-term corrosion rate for each measurement point, and produce an Excel workbook with the results."

**What the agent does:**
1. Runs OCR on the scanned PDF (vision model)
2. Extracts a structured table of thickness readings and measurement points
3. Loads historical readings from the EAM mock
4. Matches measurement points by tag, location and orientation
5. Generates Python code that:
   - Computes `CR = (t_previous − t_current) / Δt`
   - Flags points below minimum allowable thickness
   - Produces a per-point summary and an aggregate trend
6. Executes the code in the sandbox
7. Captures the Excel workbook and a thickness-trend chart
8. Returns both with the code shown and a citation to every source value

**Verification:** The engineer clicks into the generated code, sees the inputs, formula, and outputs, and either accepts or edits.

## Sandbox security controls

- No network interface (deny-all)
- Read-only access to whitelisted data directories
- Write access only to a temporary directory that is wiped after execution
- CPU limit (e.g., 2 cores)
- Memory limit (e.g., 4 GB)
- Execution time limit (e.g., 60 seconds)
- No privileged capabilities
- No access to GPU (unless explicitly granted for a specific task)
- No access to model weights or index directories
- No access to credentials or environment secrets
- Stdout, stderr and generated files captured and logged

## What the AI must NOT do in the sandbox

- Access the network
- Read files outside the whitelist
- Write to system directories
- Modify source documents
- Modify the vector index or knowledge base
- Persist across executions
- Access other users' temporary files

## Demo evidence

The demo should show:

- The generated code (visible to the judge)
- The sandbox execution log (no network, resource limits)
- The output files (Excel workbook, chart)
- The engineer's review step

## Air-gap proof

Sandbox network isolation is part of the air-gap proof. The network monitor should show zero external calls, and the sandbox log should show deny-all network policy.

## Human gate

The engineer reviews:
- The question the code is answering
- The inputs the code used
- The formula or algorithm
- The output
- The assumptions
- Any warnings or flags

Only after the engineer accepts does the result enter a document or calculation record.
