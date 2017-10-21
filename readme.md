# 重启工具

能够按照预定的时间间隔重启对应进程的小工具

- 命令行参数说明：
    - arg1 需要执行的命令行指令
    - arg2 重启间隔
- 使用示例：
    - `python restarter.py foo.bat 5`
    - `python restarter.py "ping 127.0.0.1 -t" 5`
