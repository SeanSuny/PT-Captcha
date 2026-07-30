#!/usr/bin/env python
# -*- coding:utf-8 -*-
############################################################
# @Author       : Sean
# @Date         : 2022-02-22 19:05:52
# @LastEditors  : Sean
# @LastEditTime : 2022-03-10 15:26:49
# @Description  : 这是由 Sean 创建
# @FilePath     : /run.py
# @Copyright    : Copyright ©2019-2022 Sean,Inc
############################################################

from captcha_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)