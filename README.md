# Asteroid Research since 2001

一个面向学术综述（Survey/Review）的、可持续维护的小行星研究文献数据库。工作标题为 **Asteroid Research since 2001: Surveys, Methods, Physical Characterization, and Data-Driven Approaches**；范围暂定为 2001–2026 年现代小行星研究。

本库不是按年份罗列论文，而是追踪科学问题、方法演化、可复用数据与仍未解决的局限。初期保持较宽的覆盖面；在形成 200–300 篇文献池并筛选出 landmark papers 后，再决定最终综述的聚焦方向。

## 使用方式

1. 将每篇检索到的论文录入 `bibliography/papers.csv`，并给出稳定的 DOI、ADS 或 arXiv 标识。
2. 每篇论文使用 `Main_question`、`Method`、`Innovation`、`Limitation` 四列记录可综合的分析，而非仅写摘要。
3. 依据 `Review_priority` 标为 A（基础/里程碑）、B（代表性）或 C（扩展文献）。
4. 将跨论文的结论、方法比较和待核验问题写入相应主题文件；引用键须与 `references.bib` 一致。

## 目录

- `bibliography/`：结构化文献库、BibTeX 与核心论文清单。
- `00_foundations/`：解释现代方法时不可绕过的 2001 年以前基础工作。
- `01_surveys/` 至 `10_datasets_and_software/`：按研究主题积累可直接转化为综述章节的笔记。
- `statistics/`：可复现的文献与方法趋势分析。
- `review_outline.md`：综述问题、候选叙事与逐步收敛的写作大纲。

## 范围说明

2001 年是现代大规模数字巡天与反演时代的实用起点，并非小行星研究的起点。该时期见证了 CCD 巡天、自动移动天体处理、红外测量、稀疏测光反演、空间天体测量和数据驱动方法对种群级研究的推动。

## 数据质量

只收录可追溯来源；书目信息和结论均需核验。对预印本要在 `Journal` 中标明状态。`Citations` 需注明来源与查询日期，避免把动态指标视为固定事实。
