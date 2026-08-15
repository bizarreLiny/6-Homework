# HW 1.1 学习笔记

> **日期**：2026.7.13

## 一、虚拟机安装心得

VMware已于去年打黑客松时安装完成。
遭遇到的主要困难为虚拟机网络配置，频繁出现虚拟机网络无法正常连接的问题，多次重启后恢复正常。
安装VMware工具包时也出现了诸多问题，例如文件无法传入虚拟机/复制黏贴失效等等。

## 二、Linux 常用命令总结

### 基础文件操作

- change directory: 
   - `cd <path/to/data>`
   - `cd ~`
- make directory:
   - `mkdir <name>`
- remove:
   - `rm <filename>`
- list:
   - `ls`
- View File Content:
   - `cat <filename>`
- Create a New File:
   - `cat > newfile # Type your content, then press Ctrl+D to save`




### 权限与环境变量

- print environment:
   - `printenv`
- grep (Global Regular Expression Print):
   - `grep [options] pattern [file...]`
- export:
   - `export ENVIRONMENTNAME=$`

## 三、Conda 隔离原理的个人理解

> conda创建虚拟环境的原理是通过创建一个独立的环境目录，在目录中安装所有需要的包和库，从而实现了对不同项目之间依赖的隔离。
> 每个虚拟环境都是一个完全独立的Python解释器，可以在不影响其他项目的情况下安装或更新包。
---


