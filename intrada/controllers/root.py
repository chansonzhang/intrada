from pecan import expose, redirect
from webob.exc import status_map
from intrada.controllers import v1
from intrada.controllers.api import api


class RootController(object):
    api = api.ApiController()