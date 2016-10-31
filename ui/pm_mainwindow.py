from PyQt5.Qt import QMainWindow
from model.pm_processtreemodel import PM_ProcessTreeModel
from pm_processtreewidget import PM_ProcessTreeWidget

class PM_MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Process Monitor")
        self.process_tree_widget = PM_ProcessTreeWidget(self)
        self.process_tree_model = PM_ProcessTreeModel(self)
        self.process_tree_widget.setModel(self.process_tree_model)
        # self.system_tree_model = SystemTreeModel(self, networks)
        self.setCentralWidget(self.process_tree_widget)
        self.show()