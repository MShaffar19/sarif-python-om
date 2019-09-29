# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class Invocation(object):
    """The runtime environment of the analysis tool run."""
    execution_successful = attr.ib()
    account = attr.ib(default=None)
    arguments = attr.ib(default=None)
    command_line = attr.ib(default=None)
    end_time_utc = attr.ib(default=None)
    environment_variables = attr.ib(default=None)
    executable_location = attr.ib(default=None)
    exit_code = attr.ib(default=None)
    exit_code_description = attr.ib(default=None)
    exit_signal_name = attr.ib(default=None)
    exit_signal_number = attr.ib(default=None)
    machine = attr.ib(default=None)
    notification_configuration_overrides = attr.ib(default=None)
    process_id = attr.ib(default=None)
    process_start_failure_message = attr.ib(default=None)
    properties = attr.ib(default=None)
    response_files = attr.ib(default=None)
    rule_configuration_overrides = attr.ib(default=None)
    start_time_utc = attr.ib(default=None)
    stderr = attr.ib(default=None)
    stdin = attr.ib(default=None)
    stdout = attr.ib(default=None)
    stdout_stderr = attr.ib(default=None)
    tool_configuration_notifications = attr.ib(default=None)
    tool_execution_notifications = attr.ib(default=None)
    working_directory = attr.ib(default=None)