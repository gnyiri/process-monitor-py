from pm_logger import PM_Logger


class PM_Base(object):
    """
    Base class for all PM classes
    """
    ROOT_DIRECTORY = "/proc"

    def __init__(self):
        self._logger = PM_Logger.get_instance()

    @property
    def logger(self):
        return self._logger
