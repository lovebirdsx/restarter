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
            sig = process.poll()
            if not sig is None:
                if process.returncode == 0:
                    return
                else:
                    break

        if process.poll() is None:
            system('taskkill /F /T /PID {0} 2>NUL 1>NUL'.format(process.pid))

            # 等待一段时间，避免下一次启动时由于之前的资源占用导致进程启动失败
            # 譬如cmd_file中包含输出到文件的操作
            sleep(1)


if __name__ == '__main__':
    run(argv[1], int(argv[2]))
