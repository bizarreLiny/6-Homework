# RoboCon 算法组阶段一作业规范示例

本仓库为 RoboCon 机器人竞赛算法组 **阶段一（Phase 1）** 的作业提交示例仓库，用于展示作业目录结构和交付物规范。

> **注意**：本仓库中的所有文件均为占位模板，不包含任何实质性代码或完整内容。请在完成对应作业后替换为你的实际实现。

## 快速开始

1. 克隆或复制本仓库作为作业提交模板
2. 按作业编号逐一完成，将占位文件替换为你的实际交付物
3. 参考仓库中的 `.gitignore` 配置管理你的本地仓库

## 阶段作业概览

| 作业编号 | 主题 | 核心技能 | 状态 |
|----------|------|----------|------|
| HW 1.1 | VMware 环境搭建 & Conda 隔离 | Linux 基础命令、Conda 虚拟环境管理 | 待完成 |
| HW 1.2 | Python 批处理脚本 | argparse、OpenCV、循环/条件判断/字典 | 待完成 |
| HW 1.3 | HSV 色彩空间 & 掩膜提取 | BGR->HSV、cv2.inRange、颜色阈值 | 待完成 |

## 各作业交付物清单

### HW 1.1 — VMware 环境搭建、Conda 隔离与笔记规范

| 交付物 | 文件名 | 说明 |
|--------|--------|------|
| 环境截图 | 截图图片 | `conda env list` 终端截图，直接放入文件夹 |
| 环境配置 | `environment.yml` | `conda env export` 导出 |
| 学习笔记 | `notes.md` | 虚拟机心得 + Linux 命令 + Conda 原理 |

### HW 1.2 — Python 基础语法与批处理脚本

| 交付物 | 文件名 | 说明 |
|--------|--------|------|
| Python 脚本 | `img_checker.py` | argparse + OpenCV 图像批处理 |
| 运行日志 | `output.txt` | 重定向输出的脚本运行结果 |
| 进度笔记 | `notes.md` | Python 语法问题和解决方法 |

### HW 1.3 — HSV 色彩空间转换与掩膜处理

| 交付物 | 文件名 | 说明 |
|--------|--------|------|
| Python 脚本 | `hsv_mask.py` | HSV 转换 + cv2.inRange 掩膜提取 |
| 思考题回答 | `hsv_thinking.md` | 为什么用 HSV 而非 BGR |

## 仓库结构

```
RoboCon-Training-Sample/
├── README.md
├── .gitignore
└── Phase_1/
    ├── HW_1.1/
    │   ├── notes.md
    │   └── environment.yml
    ├── HW_1.2/
    │   ├── img_checker.py
    │   ├── output.txt
    │   └── notes.md
    └── HW_1.3/
        ├── hsv_mask.py
        └── hsv_thinking.md
```

## 提交说明

1. **提交入口**：https://send2me.cn/l3LFY_TH/RpKeo3zP4xwu9Q
2. **提交方式**：将自己的仓库地址填入上述表格，之后每次完成作业 push 后在此登记即可（不再需要单独打包 zip）
3. **图片处理**：若作业中有需要提交截图/照片等图片，直接放入对应作业文件夹一同提交即可
4. **笔记格式**：所有笔记须使用 Markdown 格式编写，逻辑清晰
5. **示例仓库**：https://github.com/BeiNuoKeLi/RoboCon-Training-Sample（本仓库仅为格式参考，具体交付物以各作业要求为准）

---

*本仓库仅作格式参考，具体交付物以各作业描述为准，请基于此模板完成你的作业并提交。*
