import time

from rest_framework.throttling import BaseThrottle

VISIT_RECORD = {}


class OneInTenSecondsThrottle(BaseThrottle):
    """Честно: спёр реализацию и передалел под 1 запрос в 10 секунд"""
    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        remote_addr = self.get_ident(request)
        ctime = time.time()
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime]
            return True
        history = VISIT_RECORD.get(remote_addr)
        self.history = history
        while history and history[-1] < ctime - 10:
            history.pop()
        if len(history) < 1:
            history.insert(0, ctime)
            return True

    def wait(self):
        ctime = time.time()
        return 10 - (ctime - self.history[-1])
