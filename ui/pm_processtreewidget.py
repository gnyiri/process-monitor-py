from PyQt5.Qt import QTreeView, QSizePolicy, QMenu, Qt, QAction, QIcon, QCursor


class PM_ProcessTreeWidget(QTreeView):

    def __init__(self, parent=None):
        QTreeView.__init__(self, parent)

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.setSelectionMode(QTreeView.SingleSelection)
        self.setSelectionBehavior(QTreeView.SelectRows)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setAlternatingRowColors(True)
