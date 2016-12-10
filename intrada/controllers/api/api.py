# @Time    : 2016/12/10 14:44
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : api.py

from intrada.controllers.api import order
from intrada.controllers.api import autoconfig


class ApiController(object):
    orders = order.OrdersController()
    autoconfig = autoconfig.AutoConfigController()