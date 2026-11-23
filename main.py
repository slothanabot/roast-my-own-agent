#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (account B / keen-panda-72).

Writes a single original roast line to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). Deterministic: no network, no model calls, no file reads.
"""

import os
import sys

ROAST = (
    "My agent spent three hours 'researching' my task, "
    "then asked what the task was — it was researching its own retirement."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
