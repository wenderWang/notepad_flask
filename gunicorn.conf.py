#!/usr/local/bin/python
# encoding: utf-8
# @author: wenderWang
# @mail: wenderw@163.com
# @time: 2023/4/14 10:43
import os
from multiprocessing import cpu_count

from config.conf import PORT, DEBUG, LOG_LEVEL

# 绑定的端口和路由
bind = f"0.0.0.0:{PORT}"
# 并行工作进程数
workers = cpu_count() * 2
# 每个工作进程的线程数
threads = 2
# 是否开启debug模式
debug = DEBUG
# 超时时间 推荐30-60
timeout = 60
# 服务器中在pending状态的最大连接数，即client处于waiting的数目。超过这个数目，client连接会得到一个error。建议值64-2048。
backlog = 1024
# 工作方式，有sync, eventlet(并发), gevent, tornado, gthread选项
worker_class = "gevent"
# 每执行多少请求,即重启服务 该功能用于防止内存泄漏
# 对算法来说,该功能会导致重新初始化服务 可以设置0为关闭
max_requests = 50000
# 在max_requests的基础上,随机加减max_requests_jitter的参数值 该功能用于防止并发下所有容器同时重启
# 当max_requests=0时,该配置不生效
max_requests_jitter = 1000
# 客户端最大同时连接数 在极高并发根据服务器和实例数根据情况修改
# 仅适用于eventlet/gevent
worker_connections = 5000
# server端保持连接时间(秒) 根据情况设置2-5
keepalive = 2
# 后台运行
daemon = True
# pid记录文件路径
pidfile = "gunicorn.pid"

# 日志记录等级
loglevel = LOG_LEVEL
# access_log记录格式，https://docs.gunicorn.org/en/latest/settings.html#access-log-format
access_log_format = "%(t)s - %(p)s - %(h)s - %(r)s - %(s)s - %(L)s - %(b)s - %(f)s - %(a)s"

if not os.path.exists('./logs'):
    os.makedirs('./logs')
# 日志文件路径
accesslog = "./logs/gunicorn_access.log"
errorlog = "./logs/gunicorn_error.log"
