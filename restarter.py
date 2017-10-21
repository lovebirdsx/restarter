#coding=utf8

"""
定时重启的运行模块
"""

from subprocess import Popen
from time import sleep
from os import system
from sys import argv


def run(cmd_file, restart_interval):
    """ 运行接口 """
    while True:
        process = Popen(cmd_file)
        for _ in range(restart_interval):
            sleep(1)
            # 如果进程正常结束，则无需再次重启
            if not process.poll() is None:
                return
        system('taskkill /F /T /PID ' + str(process.pid))


if __name__ == '__main__':
    run(argv[1], int(argv[2]))
