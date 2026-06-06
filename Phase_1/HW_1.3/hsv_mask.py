"""
HW 1.3 — HSV 色彩空间转换与掩膜提取（占位模板）

功能要求：
  - 读入包含红/蓝两色比赛道具球的图片
  - 将图像从 BGR 色彩空间转换至 HSV 色彩空间
  - 根据预设的颜色阈值范围（cv2.inRange），分别提取红色球和蓝色球的二值化掩膜
  - 计算掩膜中白色像素点总数，判断哪种颜色的球占比更大

请在下方函数体中完成你的实现。
"""

import cv2
import numpy as np


def main():
    # TODO: 加载图片路径
    # TODO: cv2.imread 读取图片
    # TODO: cv2.cvtColor 转换为 HSV
    # TODO: 定义红/蓝颜色阈值范围（HSV 上下界）
    # TODO: cv2.inRange 生成二值化掩膜
    # TODO: 统计白色像素点数量，输出占比结果
    pass


if __name__ == "__main__":
    main()
