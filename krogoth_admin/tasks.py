from krogoth_admin.models import KrogothAppTrace, KrogothServerLog


class LogServerSystemProcess:
    recorded_info = {}

    def __init__(self, proc_type: str, *args, **kwargs):
        super(LogServerSystemProcess, self).__init__(proc_type, *args, **kwargs)


class konsole:

    @classmethod
    def log(input):
        ksl = KrogothServerLog(console_type="log", content=)


class LogServerHTTPRequest:
    recorded_info = {}

    def __init__(self, proc_type: str, *args, **kwargs):
        super(LogServerHTTPRequest, self).__init__(proc_type, *args, **kwargs)




