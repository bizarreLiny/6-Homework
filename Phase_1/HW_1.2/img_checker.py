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
    parser.add_argument('--dir', type=str, help='Directory containing images')


def main():
    args = parse_args()
    files = os.listdir(args.dir)
    img_count = 0
    # TODO: 筛选 .jpg / .png 文件（不区分大小写）
    print("="*42)
    for file in files:
        if file.lower().endswith(('.jpg', '.png')):
            img_count += 1
            img_path = os.path.join(args.dir, file)
            img = cv2.imread(img_path)
            if img is not None:
                height, width = img.shape[:2]
                channels = img.shape[2] if len(img.shape) == 3 else 1
                print(f"文件名: {file}\n 分辨率: {width} x {height}\n 通道数: {channels}")
                print("-"*42)
    print("="*42)
    print(f"总计: {img_count} 张图片")

if __name__ == "__main__":
    main()
