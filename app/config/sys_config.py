#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# @Time    :   2023/03/14 14:14:11
# @Author  :   wenderWang
# @mail    :   wenderw@163.com
# @Desc    :   None
from flask import Config


class BaseConfig(Config):
    SECRET_KEY = "wender"
    JSON_AS_ASSCII = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True


class TestingConfig(BaseConfig):
    ENV = "testing"
    DEBUG = False

class ProductConfig(BaseConfig):
    ENV = "product"
    DEBUG = False


Configs = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prodect": ProductConfig
}
