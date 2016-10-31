import os

from util.pm_base import PM_Base


class PM_ProcessItem(PM_Base):
    """
    Encapsulates a Linux process
    """
    ATTRIBUTES = ["Name", "Pid", "PPid"]

    def __init__(self, pid, parent=None):
        """
        :param pid: process ID (pid)
        :param name: name of the process
        :param parent: parent process (ppid)
        """
        PM_Base.__init__(self)

        assert isinstance(pid, str)

        self.logger.debug("Init process item (%s)", pid)

        self._parent = parent
        self._stat_file_path = os.path.join(PM_Base.ROOT_DIRECTORY, str(pid), "status")

        if self._parent:
            self._parent.append_child(self)

        self._children = list()
        self._data = list()

        self.update()

    @property
    def stat_file_path(self):
        return self._stat_file_path

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if value:
            self._parent = value
            self._parent.append_child(self)

    @property
    def children(self):
        return self._children

    def child(self, row):
        if 0 <= row < self.row_count():
            return self.children[row]
        return None

    def row_count(self):
        return len(self.children)

    def column_count(self):
        return len(PM_ProcessItem.ATTRIBUTES)

    def data(self, column):
        if 0 <= column < self.column_count():
            return str(self._data[column])
        return str("n/a")

    def append_child(self, child):
        assert child
        self.children.append(child)

    def row(self, child=None):
        if not child:
            if self._parent:
                return self.parent.children.index(self)
            return 0
        else:
            if child in self.children:
                return self.children.index(child)
            return 0

    def update(self):
        stat_file = open(self._stat_file_path, "r")

        assert stat_file

        self._data = list()

        for line in stat_file.readlines():
            for attribute in PM_ProcessItem.ATTRIBUTES:
                if line.startswith(attribute):
                    tokens = line.split(":")
                    assert len(tokens) > 1
                    value = line.split(":")[1].strip()
                    self._data.insert(PM_ProcessItem.ATTRIBUTES.index(attribute), value)

        self.logger.debug("%s", self._data)
