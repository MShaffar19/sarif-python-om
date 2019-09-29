# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class MultiformatMessageString(object):
    """A message string or message format string rendered in multiple formats."""
    text = attr.ib()
    markdown = attr.ib(default=None)
    properties = attr.ib(default=None)
