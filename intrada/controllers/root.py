from pecan import expose, redirect
from webob.exc import status_map
from intrada.controllers import v1


class RootController(object):
    v1 = v1.VersionController()