# @Time    : 2016/12/10 14:44
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : order.py

import pecan
from pecan import rest, response


class OrdersController(rest.RestController):
    @pecan.expose("json")
    def get(self):
        return {
            "100A": "1 bag of corn",
            "293F": "2 bags of potatoes",
            "207B": "1 bag of carrots"
        }

    @pecan.expose()
    def post(self):
        # TODO: Create a new order, (optional) return some status data
        response.status = 201
        return

    @pecan.expose()
    def put(self):
        # TODO: Idempotent PUT (return 200 or 204)
        response.status = 204
        return

    @pecan.expose()
    def delete(self):
        # TODO: Idempotent DELETE
        response.status = 200
        return