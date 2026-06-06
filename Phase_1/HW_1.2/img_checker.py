"""
HW 1.2 — 图像批处理脚本（占位模板）

功能要求：
  - 使用 argparse 接收外部文件夹路径作为输入参数
  - 遍历文件夹，筛选 .jpg / .png 图片（不区分大小写）
  - 用 OpenCV 读取图片，输出每张图片的名称、分辨率（宽 x 高）、通道数
  - 使用字典（Dict）存储并打印上述信息

执行方式：
  python img_checker.py --dir ./dataset > output.txt

请在下方函数体中完成你的实现。
"""

import argparse
import os
import cv2


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="图像批处理脚本")
    # TODO: 添加 --dir 参数
    pass


def main():
    args = parse_args()
    # TODO: 遍历目标文件夹
    # TODO: 筛选 .jpg / .png 文件（不区分大小写）
    # TODO: 用 cv2.imread 读取图片
    # TODO: 用字典存储并打印 名称、分辨率、通道数
    pass


if __name__ == "__main__":
    main()
