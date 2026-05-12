# config.py — VyaparDrishti Global Configuration
import os

# ── Paths ──────────────────────────────────────────
BASE_DIR        = os.path.dirname(os.path.abspath(__file__))
DATA_RAW        = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED  = os.path.join(BASE_DIR, "data", "processed")
MODELS_DIR      = os.path.join(BASE_DIR, "models")
REPORTS_DIR     = os.path.join(BASE_DIR, "reports")

# ── Flask ───────────────────────────────────────────
FLASK_PORT      = 5000
DEBUG           = True

# ── ML ─────────────────────────────────────────────
RANDOM_STATE    = 42
TEST_SIZE       = 0.2

print("✅ VyaparDrishti config loaded.")
