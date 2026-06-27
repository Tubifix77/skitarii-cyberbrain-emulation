# Skitarii Cyberbrain Emulation

A fork of [brain-emulation](https://github.com/Tubifix77/brain-emulation) in which
the five brain-region nodes no longer emulate a healthy human mind — they emulate a
**cybernetically converted soldier's**: emotion, personal memory, and conscience
surgically removed, leaving a cold, compliant, tactical machine. Everything else
about the program is brain-emulation, untouched.

Open it and it looks and behaves exactly like brain-emulation — same pipeline, same
UI, same comparison tabs — except the answer it produces has had the humanity
quietly taken out of it.

## What it is

brain-emulation runs your input through a short chain of "brain region" nodes —
Thalamus → Amygdala → Prefrontal Cortex → Hippocampus → Broca's Area — each a tiny
LLM prompt that adds to a shared, snowballing context, ending in a spoken-style
answer. It shows three things side by side: the raw model reply, the simulated
(brain-processed) reply, and a **Difference** analysis of what the simulation
changed.

This edition keeps all of that and rewrites **only the five region prompts** so the
mind being simulated is a converted soldier's. The payoff is the contrast: the
**Human-like LLM** answer and the **Skitarii Emulation** answer sit next to each
other, and the Difference tab — which normally reports what the simulation *added*
to feel more human — now reports what the conversion *stripped away*.

### The five regions, reworked

| Region | In brain-emulation | Here |
|---|---|---|
| **Thalamus** | Distils the request into one clean sentence | Relays it as a bare directive, with tone and emotional framing stripped off |
| **Amygdala** | Reads the user's emotion and urgency | Registers no feeling; reports the input only as a cold threat / priority level |
| **Prefrontal Cortex** | Cold logic, lists the constraints | Amoral — judges only whether an instruction can be executed efficiently, not whether it is wise, safe, or kind |
| **Hippocampus** | Recalls relevant patterns and what people typically do | No personal or autobiographical memory; retrieves only impersonal facts and procedures |
| **Broca's Area** | Warm, conversational voice matching your tone | Flat and mechanical — direct, no warmth or empathy — but still **plain readable English** |

## The root

The architecture, orchestrator, Tkinter UI, snowball context, and the
Default/Difference comparison are all [brain-emulation](https://github.com/Tubifix77/brain-emulation)'s.
The substantive change is confined to the five system prompts in `brain/nodes.py`
(plus their on-screen labels, and a dark Adeptus-Mechanicus colour theme in
`brain/config.py` and `brain/ui.py`). The pipeline and the model's generated output
were not modified — only the persona running through them, and the paint.

## The wrong direction

This is the **second** attempt. The first —
[skitarii-cortex](https://github.com/Tubifix77/skitarii-cortex) — went the wrong way,
and is kept only as a cautionary artifact.

That version threw brain-emulation's architecture out and rebuilt a Skitarii brain
from scratch: organic regions as LLM calls, excised regions as deterministic code, a
dual-channel "Bastion of Calm" partition, the source lore's equations (`A_combat`,
`Ψ_total`) wired up as live state, a command-vacuum state machine, and a binaric
"Vox-Skit-Code" output deliberately built to be the *inverse* of a readable voice.

It worked — and that was the problem. Optimising for fidelity to a being whose entire
aesthetic is incomprehensible machine-cant produced something genuinely
incomprehensible: a wall of techno-babble no human wants to read. The lesson it
taught is the whole reason this repo exists — **the interesting result was never a
faithful Skitarii, it was the contrast**: the same familiar brain, the same readable
pipeline, with the humanity removed. That contrast is only visible if the output
stays legible. So this edition does the minimum possible: change the five prompts,
keep everything else.

## Running it

Requires [Ollama](https://ollama.com/) running locally.

```bash
# 1. pull the model named in brain/config.py (default: gemma4:e2b) and start the daemon
ollama serve

# 2. launch the app
python app.py
```

Type something with a bit of emotional weight — *"my server crashed and I'm losing
money"*, *"my dog just died, what do I do"* — then compare the **Human-like LLM** tab
against the **Skitarii Emulation** final answer, and read the **Difference** tab to
see the conversion laid bare.

## Layout

- `brain/nodes.py` — the five region prompts **(this is what changed)**
- `brain/config.py` — model settings and the Mechanicus palette
- `brain/ui.py` — the Tkinter app (title, labels, theme)
- `brain/pipeline.py`, `brain/trace.py`, `brain/ollama_client.py`, `brain/mdtext.py` — the engine, carried over unchanged
- `experiments/`, `tests/` — inherited from brain-emulation
