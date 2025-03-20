from ui.EmployeeManagement import Ui_mainWindow


class EmployeeManagementExt(Ui_mainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
        self.MainWindow.show()