# Skills

自用的 skills 集合，可通过 `skills` CLI 一键安装。

## 安装

```bash
npx skills add https://github.com/jiang-zhexin/skills
```

## 结构

```plaintxt
skills
└── arxiv-translator                  # 将 arXiv 论文自动翻译为中文 PDF
    ├── SKILL.md
    ├── scripts/
    │   └── download.py               # 下载 LaTeX 源码
    └── references/
        └── tectonic.md               # tectonic 编译参数参考
```
