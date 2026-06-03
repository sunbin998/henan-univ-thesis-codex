#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require(path: str) -> Path:
    target = ROOT / path
    if not target.exists():
        fail(f"Missing required path: {path}")
    return target


def validate_frontmatter() -> None:
    skill = require("SKILL.md")
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        _, frontmatter, body = text.split("---", 2)
    except ValueError:
        fail("SKILL.md frontmatter must be delimited by ---")
    if not body.strip():
        fail("SKILL.md must contain body instructions")

    keys = []
    for line in frontmatter.splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            keys.append(match.group(1))

    if keys != ["name", "description"]:
        fail(f"SKILL.md frontmatter keys must be exactly name, description; got {keys}")
    if "henan-univ-thesis" not in frontmatter:
        fail("SKILL.md frontmatter must name the skill")
    if len(text.splitlines()) > 500:
        fail("SKILL.md should stay under 500 lines")


def validate_structure() -> None:
    for path in [
        "README.md",
        "LICENSE",
        "assets/logo.png",
        "references",
        "scripts",
        "evals/evals.json",
    ]:
        require(path)

    references = sorted((ROOT / "references").glob("*.md"))
    if len(references) < 6:
        fail("Expected at least six reference markdown files")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "assets/logo.png" not in readme:
        fail("README.md must reference assets/logo.png")
    if "quick_validate.py" not in readme:
        fail("README.md should document skill validation")


def validate_evals() -> None:
    evals_path = require("evals/evals.json")
    data = json.loads(evals_path.read_text(encoding="utf-8"))
    if data.get("skill_name") != "henan-univ-thesis":
        fail("evals/evals.json skill_name must be henan-univ-thesis")
    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        fail("evals/evals.json must contain non-empty evals list")
    for item in evals:
        for key in ["id", "prompt", "expected_output", "files"]:
            if key not in item:
                fail(f"Eval item missing key: {key}")


def validate_no_junk() -> None:
    junk_patterns = [
        "*Zone.Identifier*",
        "__pycache__",
        "*.pyc",
        ".codex-write-test",
    ]
    for pattern in junk_patterns:
        matches = [p for p in ROOT.rglob(pattern) if ".git" not in p.parts]
        if matches:
            fail(f"Unexpected junk files: {', '.join(str(p.relative_to(ROOT)) for p in matches)}")


def main() -> None:
    validate_frontmatter()
    validate_structure()
    validate_evals()
    validate_no_junk()
    print("Skill repository validation passed.")


if __name__ == "__main__":
    main()
