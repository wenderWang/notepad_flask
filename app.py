#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# @Time    :   2023/03/14 14:03:43
# @Author  :   wenderWang
# @mail    :   wenderw@163.com
# @Desc    :   None
from flask import Flask

from config.conf import ENV, PORT
from app.config.sys_config import Configs


def create_app():
    """
    初始化flask app
    """
    app = Flask(__name__)
    app.config.from_object(Configs[ENV])

    return app


if __name__ == "__main__":
    create_app().run(port=PORT)
