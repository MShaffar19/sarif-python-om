# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class ArtifactLocation(object):
    """Specifies the location of an artifact."""
    description = attr.ib(default=None)
    index = attr.ib(default=-1)
    properties = attr.ib(default=None)
    uri = attr.ib(default=None)
    uri_base_id = attr.ib(default=None)
