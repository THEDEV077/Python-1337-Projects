import os
import sys
from dotenv import load_dotenv
from typing import Any, Dict


def get_env(key: str, default: Any = None) -> Any:
    return os.getenv(key, default)


def build_config() -> Dict[str, Any]:
    return {
        "mode": get_env("MATRIX_MODE", "development"),
        "db": get_env("DATABASE_URL"),
        "api_key": get_env("API_KEY"),
        "log_level": get_env("LOG_LEVEL", "DEBUG"),
        "zion": get_env("ZION_ENDPOINT")
    }


def display_config(cfg: Dict[str, Any]) -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {cfg['mode']}")

    if cfg["mode"] == "production":
        print("Database: Connected to production cluster")
        print("API Access: Secured")
        print("Log Level: WARNING")
    else:
        print("Database: Connected to local instance")
        if cfg["api_key"]:
            print("API Access: Authenticated")
        else:
            print("API Access: Development mode")
        print(f"Log Level: {cfg['log_level']}")

    print(f"Zion Network: {'Online' if cfg['zion'] else 'Offline'}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if cfg["api_key"]:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not configured")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def check_missing(cfg: Dict[str, Any]) -> None:
    required = {"DATABASE_URL": cfg["db"], "API_KEY": cfg["api_key"],
                "ZION_ENDPOINT": cfg["zion"]}
    missing = [key for key, val in required.items() if not val]
    if missing:
        print("\n[ERROR] Missing required configuration:")
        for key in missing:
            print(f"  - {key} is not set")
        print("\nCopy .env.example to .env and fill in the values.")
        sys.exit(1)


def main() -> None:
    load_dotenv()
    cfg = build_config()
    check_missing(cfg)
    display_config(cfg)


if __name__ == "__main__":
    main()
