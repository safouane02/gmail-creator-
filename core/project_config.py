#!/usr/bin/env python3
"""Central project identity and path configuration."""

from pathlib import Path

PROJECT_NAME = "gmail by safouane"
PROJECT_VERSION = "2026.1.0"
PROJECT_AUTHOR = "safouane02.github"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
CREDENTIALS_DIR = PROJECT_ROOT / "credentials"
LOGS_DIR = PROJECT_ROOT / "logs"
OUTPUT_DIR = PROJECT_ROOT / "output"

FINGERPRINTS_FILE = CONFIG_DIR / "fingerprints.json"
SETTINGS_FILE = CONFIG_DIR / "settings.yaml"
PROXIES_FILE = CONFIG_DIR / "proxies.txt"
SUCCESS_FILE = OUTPUT_DIR / "successful_accounts.json"
ERROR_FILE = OUTPUT_DIR / "failed_attempts.json"
PROFILES_DIR = CREDENTIALS_DIR / "profiles"


def ensure_runtime_directories() -> None:
    """Create runtime directories if they do not already exist."""
    for dir_path in [CONFIG_DIR, CREDENTIALS_DIR, LOGS_DIR, OUTPUT_DIR, PROFILES_DIR]:
        dir_path.mkdir(parents=True, exist_ok=True)
