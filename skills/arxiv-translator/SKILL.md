---
name: arxiv-translator
description: 将 arXiv 论文自动翻译为中文 PDF。触发后按本 skill 三步顺序直接执行，勿长篇规划。用户提供 arXiv ID、说「翻译论文」「我想读中文版」等时立即使用。无需用户手动操作。
---

# arXiv 论文中文翻译

**目标：** 将指定论文的 LaTeX 源码译为中文，并编译得到 PDF。

**流程：** 须严格按下文「第一步」至「第三步」顺序执行，不得擅自省略、合并或调换步骤。

**交互：** 仅在论文 ID 无法确定、检索结果存在多个需用户择一才可向用户提问；其余情况一律无中断的执行得到最终翻译后的PDF。

**翻译：** 翻译全部由当前对话模型自身完成，严禁使用外部翻译工具以及下载已有的翻译版本。

## 第一步：下载 latex 源码

使用以下脚本下载 latex 源码。

```bash
uv run scripts/download.py <arxiv_id>
```

脚本最终输出 latex 下载完成的目录：

```plaintxt
success download: {OUTPUT_DIR}
```

## 第二步：翻译

由当前**对话模型**直接在原 `.tex` 文件上进行翻译修改，按以下规则翻译：

- **翻译范围：** 默认只翻正文，不翻附录，但附录中的内容需要得到保留，若同一文件中出现 `\appendix`，默认只翻该命令之前的内容。用户明确要求“翻译全文”时才翻附录。
- **必须翻译：** 正文叙述、摘要、图表标题、列表项、脚注中的描述文本，以及代码块中的注释。
- **保留不翻：** 数学环境、LaTeX 命令、`\cite{}`/`\ref{}`/`\label{}`、图片路径、URL、代码本体、`.bib`、人名、机构名、模型名、数据集名。
- **专有名词：** Transformer、Softmax、Token 等通用学术术语保留英文，不要生硬硬译。
- **标题要求：** `\title{}` 须改为自然中文题名，不保留英文原题或中英并列；输出 PDF 文件名仍使用第二步的 `PDF_NAME`。
- **多篇处理：** 多篇论文可以分别处理；只有在用户**明确要求**并行委派时，才开启多个 subagent，否则直接顺序完成。

## 第三步：编译

编译 latex 使用 tectonic。

> Tectonic is a modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive.

如果用户未安装 tectonic，则引导用户到 https://tectonic-typesetting.github.io/en-US/install.html 进行安装后再进行编译。

[完整命令行参数](references/tectonic.md)。

```bash
tectonic <file_path>
```

编译完成后输出 PDF 保存路径。
