# RoboCon 算法组阶段一作业规范示例

本仓库为 RoboCon 机器人竞赛算法组 **阶段一（Phase 1）** 的作业提交仓库。


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

