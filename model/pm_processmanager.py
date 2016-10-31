import os

from util.pm_base import PM_Base
from pm_processitem import PM_ProcessItem


class PM_ProcessManager(PM_Base):

    def __init__(self):
        PM_Base.__init__(self)
        self._processes = dict()
        self.update()

    @property
    def processes(self):
        return self._processes

    @processes.setter
    def processes(self, value):
        self._processes = value

    def update(self):
        self.logger.debug("Collect process id-s ..")
        self.processes = dict()
        process_ids = [f for f in os.listdir(PM_ProcessManager.ROOT_DIRECTORY) if f.isdigit()]

        for pid in process_ids:
            process_dir = os.path.join(PM_ProcessManager.ROOT_DIRECTORY, pid)
            self.processes[pid] = PM_ProcessItem(pid)

        self.logger.debug("%d processes found! Relocate parent items ..", len(self.processes))

        name_idx = PM_ProcessItem.ATTRIBUTES.index("Name")
        assert 0 <= name_idx < len(PM_ProcessItem.ATTRIBUTES)
        parent_idx = PM_ProcessItem.ATTRIBUTES.index("PPid")
        assert 0 <= parent_idx < len(PM_ProcessItem.ATTRIBUTES)

        for process_item in self.processes.values():
            name = process_item.data(name_idx)
            parent_pid = process_item.data(parent_idx)
            self.logger.debug("Parent of %s is %s", name, parent_pid)

            if parent_pid in self.processes.keys():
                process_item.parent = self.processes[parent_pid]
            else:
                self.logger.warn("No parent process for %s", name)

