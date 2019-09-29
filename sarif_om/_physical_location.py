# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class PhysicalLocation(object):
    """A physical location relevant to a result. Specifies a reference to a programming artifact together with a range of bytes or characters within that artifact."""
    address = attr.ib(default=None)
    artifact_location = attr.ib(default=None)
    context_region = attr.ib(default=None)
    properties = attr.ib(default=None)
    region = attr.ib(default=None)
