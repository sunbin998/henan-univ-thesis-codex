# Contributing

Thanks for improving `henan-univ-thesis`. This repository is a Codex skill for 河南科技大学本科毕业设计（论文） workflows, so contributions should keep the skill concise, practical, and safe for thesis refinement.

## What To Contribute

- Better河南科技大学 thesis format rules verified against official templates or teacher comments.
- New reference workflows under `references/` for fragile DOCX, OOXML, screenshot, citation, or rendering tasks.
- Focused improvements to `scripts/` when a repeatable operation needs deterministic behavior.
- Eval cases under `evals/` that describe realistic user prompts and expected skill behavior.
- README improvements that help users install and understand the skill.

## What Not To Include

- Real student thesis documents, private screenshots, teacher names, account credentials, or personal data.
- Large generated artifacts such as PDFs, DOCX files, page renders, or temporary images.
- Unverified formatting rules based only on generic thesis advice.
- Broad rewrites of `SKILL.md` that duplicate detailed reference files.

## Skill Design Rules

- Keep `SKILL.md` short and navigational.
- Put detailed workflows in `references/`.
- Prefer official school templates and teacher comments over inferred rules.
- Do not encourage full-document regeneration for final-stage DOCX refinement.
- Mention rendering QA when a workflow can affect final visual layout.

## Development Checklist

Before opening a pull request:

1. Check that `SKILL.md` frontmatter contains only `name` and `description`.
2. Keep new files inside the skill repository; do not include parent thesis workspace files.
3. Run the validation workflow locally when possible:

   ```bash
   python .github/scripts/validate_skill.py
   ```

4. Check git status and make sure no temporary files are staged:

   ```bash
   git status --short
   ```

## Pull Request Notes

In your PR description, include:

- What workflow or rule changed.
- Which file(s) changed.
- Whether the change is based on an official template, teacher comment, prior successful workflow, or general cleanup.
- Validation result.
