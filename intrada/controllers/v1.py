# @Time    : 2016/12/9 17:52
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : v1.py

import pecan
from pecan import rest


class VersionController(rest.RestController):
    @pecan.expose('json')
    def get(self):
        return {"version": "1.0.0"}