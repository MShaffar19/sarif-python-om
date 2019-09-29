# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class Attachment(object):
    """An artifact relevant to a result."""
    artifact_location = attr.ib()
    description = attr.ib(default=None)
    properties = attr.ib(default=None)
    rectangles = attr.ib(default=None)
    regions = attr.ib(default=None)
