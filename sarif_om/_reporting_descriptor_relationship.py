# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class ReportingDescriptorRelationship(object):
    """Information about the relation of one reporting descriptor to another."""
    target = attr.ib()
    description = attr.ib(default=None)
    kinds = attr.ib(default=['relevant'])
    properties = attr.ib(default=None)
