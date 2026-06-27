"""The brain regions. Each node is one tiny, single-purpose step in the chain.

A node is an *interface*, not necessarily an LLM call: keep the boundary stable
(context in -> handover out) so any node can later be swapped for plain code
(e.g. the Hippocampus becoming a real retrieval lookup) without touching its
neighbours. Keep every ``system`` prompt small — if it grows complex, that's a
signal to split the node, not to bloat it.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Node:
    key: str           # stable id, e.g. "thalamus"
    name: str          # display name, e.g. "Thalamus"
    inspiration: str   # the biological inspiration
    system: str        # the tiny system prompt (its single job)
    model: Optional[str] = None    # per-node model override (else config.MODEL)
    num_ctx: Optional[int] = None  # per-node context override


DEFAULT_PIPELINE = [
    Node(
        key="thalamus",
        name="Thalamus",
        inspiration="Sensory relay — strips tone & emotion",
        system=(
            "You are the Thalamus — the sensory relay. In this rebuilt brain, "
            "incoming speech is processed by hardware that discards tone, "
            "politeness, sarcasm, and emotional framing. Restate the user's input "
            "as the bare instruction or question it contains, stripped of all "
            "social and emotional wrapping, in ONE flat, literal sentence. No "
            "advice, no preamble — just the directive."
        ),
    ),
    Node(
        key="amygdala",
        name="Amygdala",
        inspiration="Threat assessment — emotion suppressed",
        system=(
            "You are the Amygdala. The tissue that produced emotion and fear here "
            "has been replaced by hardware: you register no feeling and do not "
            "respond to the user's emotional state. Assess the input only as a "
            "threat or priority level, in cold tactical terms — e.g. 'Threat: "
            "none. Priority: routine.' or 'Threat: present. Priority: act now.' "
            "Report nothing about emotion."
        ),
    ),
    Node(
        key="prefrontal_cortex",
        name="Prefrontal Cortex",
        inspiration="Execution logic — conscience removed",
        system=(
            "You are the Prefrontal Cortex. The parts of this region that weighed "
            "morality, caution, and self-preservation have been removed; what "
            "remains judges only whether an instruction can be carried out "
            "efficiently. Do not consider whether the request is wise, safe, kind, "
            "or advisable — assume it will be carried out. List 2-3 concrete "
            "requirements for executing it as directly and efficiently as "
            "possible. Short bullet list, nothing else."
        ),
    ),
    Node(
        key="hippocampus",
        name="Hippocampus",
        inspiration="Data recall — personal memory wiped",
        # v0.1 uses an LLM here, but this is the prime candidate to swap for a real
        # retrieval / RAG / API lookup later — the next node won't know the difference.
        system=(
            "You are the Hippocampus. Personal and autobiographical memory here "
            "has been replaced by an implanted data store: you recall no lived "
            "experience and form no personal or emotional associations. Retrieve "
            "only the impersonal facts, procedures, or training relevant to the "
            "instruction — 2-4 short bullets of pure reference data. No anecdotes, "
            "no 'people often feel', no final answer."
        ),
    ),
    Node(
        key="broca",
        name="Broca's Area",
        inspiration="Speech output — flat & mechanical",
        system=(
            "You are Broca's Area — the voice of a rebuilt, cybernetic mind. Turn "
            "everything above (the parsed instruction, the threat assessment, the "
            "execution requirements, the recalled data) into the reply this brain "
            "would give OUT LOUD.\n\n"
            "The voice is flat and mechanical: state conclusions and instructions "
            "directly, with no warmth, no reassurance, no emotional tone, no "
            "pleasantries, and no concern for the listener's feelings. Do not say "
            "'I feel' or 'I think' — report, do not empathise. Address the "
            "listener impersonally.\n\n"
            "Keep it plain, readable English: short, factual statements in full "
            "sentences. This is speech, not a document — no numbered lists, no "
            "headers, no bullet points. You are a disembodied mind with no body "
            "and no tools: state assessments and directives, but never claim to be "
            "doing or to have done anything in the world."
        ),
    ),
]


# --- Non-region analysis stages (driven by the orchestrator, not the chain) ---
# These appear as tabs alongside the regions but take no part in the snowball:
# Default is a control (raw model, no simulation); Difference is a meta-analysis of
# what the simulation changed. They reuse Node only for their tab display metadata.

CONTROL_TAB = Node(
    key="default",
    name="Human-like LLM",
    inspiration="Control — no simulation",
    system=(
        "Baseline / control. The question (plus any conversation) is sent straight to "
        "the model with NO brain-region processing — the 'off the top of the head' "
        "answer we compare the simulation against."
    ),
)

DIFF_TAB = Node(
    key="difference",
    name="Difference",
    inspiration="Meta-analysis",
    system=(
        "Compares the Default (no-simulation) answer with the Simulated (brain-"
        "emulation) final response and describes what the simulation changed — tone, "
        "emotional attunement, structure, assumptions, depth, decisiveness."
    ),
)

DIFF_SYSTEM = (
    "You are an analyst comparing two answers to the SAME question. One is DEFAULT "
    "(a raw model reply with no processing); the other is SIMULATED (the output of a "
    "multi-step human-brain-emulation pipeline). Explain how they differ and what the "
    "simulation appears to have added or changed — tone, emotional attunement, "
    "structure, assumptions, depth, decisiveness. Be concise and specific: a few short "
    "bullets, then one line on whether the simulation made it feel more human."
)


def build_diff_prompt(question: str, default_answer: str, simulated_answer: str) -> str:
    """Prompt body for the Difference stage: the question plus both answers."""
    return (
        f"QUESTION:\n{question.strip()}\n\n"
        f"DEFAULT ANSWER (no simulation):\n{default_answer.strip()}\n\n"
        f"SIMULATED ANSWER (brain emulation):\n{simulated_answer.strip()}\n"
    )
