<p align="center">
  <img src="assets/logo.png" alt="Henan University Thesis Codex logo" width="180">
</p>

# Henan University Thesis Codex Skill

`henan-univ-thesis` is a Codex skill for assisting with 河南科技大学本科毕业设计（论文） writing, DOCX refinement, template migration, teacher-comment handling, citation formatting, diagram replacement, screenshot insertion, and final Word/PDF layout QA.

This repository contains the skill itself. It does not contain a student's thesis document, private project source code, or school-only confidential material.

## What It Helps With

- 河南科技大学论文 / 河科大毕设 / 本科毕业论文 format workflows
- DOCX 精修：字体、字号、标题、表格、页眉页脚、目录、分页
- 官方模板迁移：以学校模板和老师批注为最高优先级
- 老师批阅版处理：先提取批注，再分批修改与复验
- 引文格式修复：正文方括号上标、参考文献顺序和引用覆盖检查
- 图表与截图：软件工程图审查、DOCX 内嵌图片替换、浏览器真实界面截图插入
- 渲染验收：DOCX 导出 PDF，再逐页检查最终视觉排版

## Repository Layout

```text
henan-univ-thesis/
├── SKILL.md
├── README.md
├── assets/
│   └── logo.png
├── references/
│   ├── citation-rules.md
│   ├── docx-refinement-workflow.md
│   ├── format-samples.md
│   ├── image-and-diagram-workflow.md
│   ├── render-qa.md
│   ├── teacher-comments-workflow.md
│   └── template-migration.md
├── scripts/
│   └── generate_docx.py
└── evals/
    └── evals.json
```

## Install

Clone or copy this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/sunbin998/henan-univ-thesis-codex.git ~/.codex/skills/henan-univ-thesis
```

After installation, Codex can trigger the skill when the user asks about 河南科技大学论文、河科大毕设、本科毕业论文、DOCX 格式精修、官方模板迁移、老师批注处理、图表与截图插入或引文格式修复.

## Usage Examples

```text
请帮我检查河南科技大学本科毕业论文的 DOCX 格式，重点看标题、表格和页眉页脚。
```

```text
老师批阅版里有摘要、目录、章标题空行和参考文献批注，请先提取批注并给出处理顺序。
```

```text
帮我把正文里的普通 [1] 引用改成方括号上标，并检查参考文献是否都被正文引用。
```

```text
论文里的图 5-1 已经有图题和图片位置，请替换 DOCX 内部嵌入图片并保持原来的版式。
```

## Core Principles

- Official school templates and teacher comments take priority.
- Directly refine existing `.docx` files during the final thesis stage.
- Do not regenerate a polished thesis with a script unless bulk structured generation is required.
- Check actual OOXML details, not only Word style names.
- Treat rendering as part of the work: export DOCX to PDF and inspect page images.
- Preserve manually refined formatting, figure captions, pagination, and citation order.

## Validation

Run the skill validator:

```bash
python /path/to/skill-creator/scripts/quick_validate.py /path/to/henan-univ-thesis
```

The current version was validated with `quick_validate.py`.

## Notes

The bundled `scripts/generate_docx.py` is kept as an auxiliary script for framework generation or batch structured content. It is not the default workflow for final-stage thesis refinement.
