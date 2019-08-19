# !/usr/bin/python
# -*- coding:utf-8 -*-


import os
import configparser



config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
print(os.path.abspath('.'))
print(file_path)