# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class ExternalPropertyFileReference(object):
    """Contains information that enables a SARIF consumer to locate the external property file that contains the value of an externalized property associated with the run."""
    guid = attr.ib(default=None)
    item_count = attr.ib(default=-1)
    location = attr.ib(default=None)
    properties = attr.ib(default=None)