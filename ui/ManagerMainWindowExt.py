from PyQt6.QtWidgets import QMainWindow

from ui.EmployeeManagementExt import EmployeeManagementExt
from ui.ManagerMainWindow import Ui_MainWindow
from ui.MaterialManagementExt import MaterialManagementExt


class ManagerMainWindowExt(QMainWindow, Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainWindow = QMainWindow()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonMaterialManagement.clicked.connect(self.show_material_management)
        self.pushButtonEmployeeManagement.clicked.connect(self.show_employee_management)

    def show_material_management(self):
        self.material_management_window = QMainWindow()
        self.ui_material_management = MaterialManagementExt()
        self.ui_material_management.setupUi(self.material_management_window)
        self.material_management_window.show()

    def show_employee_management(self):
        self.employee_management_window = QMainWindow()
        self.ui_employee_management = EmployeeManagementExt()
        self.ui_employee_management.setupUi(self.employee_management_window)
        self.employee_management_window.show()