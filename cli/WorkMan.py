# -*- coding: utf-8 -*-
import inspect
from mio.util.Logs import LogHandler


class Daemon(object):
    def __get_logger__(self, name: str) -> LogHandler:
        name = f"{self.__class__.__name__}.{name}"
        return LogHandler(name)

    def do_test(self, app, kwargs):
        id(app), id(kwargs)
        console_log = self.__get_logger__(inspect.stack()[0].function)
        console_log.info("开始干活")
        console_log.info("打完收工")
