#coding=utf8

"""
模拟退出进程，90%概率以非0退出，10%概率以0退出
"""

import sys
from random import random

if __name__ == '__main__':
    sys.exit(0 if random() < 0.1 else 1)
    
