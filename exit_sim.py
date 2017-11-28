#coding=utf8

"""
模拟进程运行一段时间，然后以正常或者非正常情况退出
"""

import sys
from random import random
from time import sleep

def main():
    """ 主函数 """

    run_time = 1.5 * random()
    exit_num = 0 if random() < 0.4 else 1
    print 'run_time = {0} exit_num = {1}'.format(run_time, exit_num)
    sleep(run_time)
    sys.exit(exit_num)

if __name__ == '__main__':
    main()
