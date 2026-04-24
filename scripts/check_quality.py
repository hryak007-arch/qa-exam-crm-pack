import subprocess
import sys

COMMANDS = [
    [sys.executable, "-m", "ruff", "check", "."],
    [sys.executable, "-m", "ruff", "format", "--check", "."],
    [sys.executable, "-m", "mypy", "."],
    [sys.executable, "-m", "pytest"],
]

for cmd in COMMANDS:
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)

print("All quality checks passed.")
