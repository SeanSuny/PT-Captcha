#!/usr/bin/env python
# -*- coding:utf-8 -*-
############################################################
# @Author       : Sean
# @Date         : 2022-03-01 14:00:23
# @LastEditors  : Sean
# @LastEditTime : 2022-03-03 15:05:47
# @Description  : 这是由 Sean 创建
# @FilePath     : d:/我的文件/0-项目/Python/pt_captcha/captcha_app/__init__.py
# @Copyright    : Copyright ©2019-2022 Sean,Inc
############################################################

from flask import Flask
from captcha_app.app import captcha_blue


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(captcha_blue)
    return app
