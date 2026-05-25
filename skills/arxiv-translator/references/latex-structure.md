# LaTeX 结构参考 —— 用于翻译分块

## 章节命令（自然分块点）

按优先级排序：

| 命令               | 级别 | 说明                   |
| ------------------ | ---- | ---------------------- |
| `\part{}`          | -1   | 极少用，论文中一般没有 |
| `\chapter{}`       | 0    | 仅 book/report 类      |
| `\section{}`       | 1    | **主要分块点**         |
| `\subsection{}`    | 2    | 补充分块点             |
| `\subsubsection{}` | 3    | 一般不分到此粒度       |

分块以 `\section{}` 为界，每块 1-2 个 section。若单个 section 超过 300 行，可在 `\subsection{}` 处再分。

## 需要保持完整的环境（不可跨块切割）

以下环境必须包含在同一个翻译块中，不能切开：

- `\begin{figure}...\end{figure}` — 浮动图
- `\begin{table}...\end{table}` — 浮动表
- `\begin{algorithm}...\end{algorithm}` — 算法
- `\begin{equation}...\end{equation}` — 单行公式
- `\begin{align}...\end{align}` — 多行公式
- `\begin{verbatim}...\end{verbatim}` — 逐字输出
- `\begin{lstlisting}...\end{lstlisting}` — 代码块
- `\begin{tikzpicture}...\end{tikzpicture}` — TikZ 图
- `\begin{theorem}...\end{theorem}` 等定理环境

## 附录分界

`\appendix` 命令标志着正文与附录的边界。该命令之前的内容翻译，之后只保留原样不翻。

注意：有些论文使用 `\begin{appendices}...\end{appendices}` 环境，也视为附录边界。

## 常见不翻译内容模式

```
\documentclass[...]{...}     — 文档类声明
\usepackage[...]{...}        — 宏包加载
\newcommand{\foo}{...}       — 自定义命令定义
\newenvironment{foo}{...}{...} — 环境定义
\bibliographystyle{...}      — 参考文献样式
\bibliography{...}           — 参考文献数据库
\begin{equation}...\end{equation} — 数学环境（全部不翻）
$$ ... $$                     — 行间数学
$ ... $                       — 行内数学
\cite{...}                    — 引用
\ref{...}, \label{...}       — 交叉引用
\includegraphics[...]{...}   — 图片
\url{...}, \href{...}{...}   — 链接
\SI{...}{...}                 — 单位（siunitx）
\acrshort{...}, \acrlong{...} — 缩写展开（glossaries）
```

## 危险区域（慎改，易导致编译失败）

以下内容尽量完全不动：

1. `\documentclass` 及其可选参数
2. 导言区（`\begin{document}` 之前的所有内容）
3. `\maketitle` 及标题页相关命令
4. 任何 `\def\foo{...}` 或 `\let\foo\bar` 形式的命令定义
5. `\catcode`, `\lccode`, `\sfcode` 等 TeX 底层命令
6. `\if...\fi` 条件判断块
