"""Central configuration: model, context window, Ollama endpoint, and UI palette.

Everything tweakable lives here so a v0.1 prototype run is one edit away from a
different model or a wider context window.
"""

# --- LLM / Ollama -----------------------------------------------------------
OLLAMA_HOST = "http://localhost:11434"

# Brand-new small, efficient Gemma variant already pulled on this machine.
# NOTE: the "e" in "e2b" is part of the model name (an efficient edge build),
# not a typo. It's quick and good enough for v0.1 prototype testing.
MODEL = "gemma4:e2b"

# Ollama defaults num_ctx to ~2k-4k tokens, which the growing "snowball" context
# will overflow and silently truncate. Override it so the whole chain's handover
# history fits. e2b is tiny, so a generous window is cheap on a 10 GB card.
NUM_CTX = 16384

# Per-request timeout (seconds) for a streaming call to Ollama.
REQUEST_TIMEOUT = 180

# --- UI palette (Adeptus Mechanicus: black iron, blood red, brass) ----------
BG_DARK = "#0f0d0d"
SIDEBAR_BG = "#161112"
PANEL_LEFT = "#1b1513"   # node job / system prompt   (dark iron)
PANEL_MID = "#15110c"    # live thinking              (brass-black)
PANEL_RIGHT = "#121611"  # handover to next step      (gunmetal-green)
FINAL_BG = "#1c0f0f"     # final response panel       (blood-dark)

ACCENT = "#9e1b1b"
ACCENT_TEXT = "#f3e7cd"
TEXT = "#e9e0cd"
MUTED = "#8f8470"
SUCCESS = "#86a85a"
ERROR = "#e5576f"

LABEL_LEFT = "#c9a227"
LABEL_MID = "#d98a3d"
LABEL_RIGHT = "#9ac77a"

FONT_UI = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 11, "bold")
FONT_TITLE = ("Segoe UI", 13, "bold")
FONT_MONO = ("Consolas", 10)
