# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class ReportingDescriptorReference(object):
    """Information about how to locate a relevant reporting descriptor."""
    guid = attr.ib(default=None)
    id = attr.ib(default=None)
    index = attr.ib(default=-1)
    properties = attr.ib(default=None)
    tool_component = attr.ib(default=None)