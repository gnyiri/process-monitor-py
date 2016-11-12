import sys
import getopt
from PyQt5.Qt import QApplication

from ui.pm_mainwindow import PM_MainWindow
from util.pm_logger import PM_Logger


def print_help():
    pass


if __name__ == '__main__':
    logger = PM_Logger.get_instance()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
        # parse command line arguments
        for opt, arg in opts:
            if opt == '-h' or opt == '--help':
                print_help()
                sys.exit()
            else:
                print_help()
                sys.exit()
    except getopt.GetoptError:
        print_help()

    logger.debug("Start application")

    APP = QApplication(sys.argv)
    ui = PM_MainWindow()
    ui.show()
    sys.exit(APP.exec_())
