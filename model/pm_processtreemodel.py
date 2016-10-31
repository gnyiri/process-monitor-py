from PyQt5.QtCore import QAbstractItemModel, QVariant, QModelIndex, Qt

from model.pm_processmanager import PM_ProcessManager
from pm_processitem import PM_ProcessItem
from util.pm_base import PM_Base


class PM_ProcessTreeModel(QAbstractItemModel, PM_Base):
    """
    Encapsulates the Linux process hierarchy and acts as a model for the
    associated QTreeView
    """

    def __init__(self, parent=None):
        PM_Base.__init__(self)
        QAbstractItemModel.__init__(self, parent)

        self.manager = PM_ProcessManager()
        self._root = self.manager.processes["1"]
        # self._root = PM_ProcessItem(0, "Operating System")
        # child = PM_ProcessItem(1, "1", self._root)

    def columnCount(self, parent=None, *args, **kwargs):
        if parent.isValid():
            parent_item = parent.internalPointer()
            return parent_item.column_count()
        else:
            return self._root.column_count()

    def rowCount(self, parent=None, *args, **kwargs):
        if not parent or parent.column() > 0:
            return 0
        parent_item = parent.internalPointer() if parent.isValid() else self._root
        return parent_item.row_count()

    def data(self, index, role=None):
        item = index.internalPointer() if index.isValid() else self._root

        if role == Qt.DisplayRole:
            return item.data(index.column())
        elif role == Qt.DecorationRole:
            return QVariant()
        elif role == Qt.ToolTipRole:
            return QVariant()
        else:
            return QVariant()

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        return QAbstractItemModel.flags(self, index)

    def headerData(self, section, orientation, role=None):
        if (orientation, role) == (Qt.Horizontal, Qt.DisplayRole):
            if 0 <= section < len(PM_ProcessItem.ATTRIBUTES):
                return PM_ProcessItem.ATTRIBUTES[section]
        return QVariant()

    def index(self, row, column, parent=None):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        parent_item = parent.internalPointer() if parent.isValid() else self._root
        child_item = parent_item.child(row)
        index = self.createIndex(row, column, child_item) if child_item else QModelIndex()
        return index

    def parent(self, index=None):
        if not index.isValid():
            return QModelIndex()
        item = index.internalPointer()
        if not item:
            return QModelIndex()
        parent_item = item.parent
        if not parent_item:
            return QModelIndex()
        index = self.createIndex(parent_item.row(), 0, parent_item)
        return index



