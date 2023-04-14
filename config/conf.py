#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# @Time    :   2023/03/14 14:16:50
# @Author  :   wenderWang
# @mail    :   wenderw@163.com
# @Desc    :   None
import os
import pytz

from dotenv import find_dotenv, load_dotenv

# 读取.env文件，转化为环境变量
load_dotenv(find_dotenv(".env"))

# *********************   BASE   *********************
ENV = os.getenv("ENV")
DEBUG = ENV == "dev"
TZ = pytz.timezone(os.getenv("TZ"))
PORT = os.getenv("PORT")
LOG_LEVEL = os.getenv("LOG_LEVEL")

# ********************* DATABASE *********************
# MYSQL
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_DB = os.getenv("DB")
MYSQL_CHARSET = os.getenv("MYSQL_CHARSET")

# REDIS
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_CACHE_DB = int(os.getenv("REDIS_CACHE_DB", 0))
