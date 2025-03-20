class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButtonExit.clicked.connect(self.process_exit)
        self.radioButtonManager.clicked.connect(self.show_manager)
        self.radioButtonEmployee.clicked.connect(self.show_material_management)
    def process_login(self):
        dc=DataConnector()
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        emp = dc.login(uid, pwd)
        if emp != None:
            self.MainWindow.close()#close login window
            self.mainwindow = QMainWindow()
            self.myui = MaterialManagement()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()
    def process_exit(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Chắc chắn thoát?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()
    def show_manager(self):
        self.manager_window = QMainWindow()
        self.ui_manager = ManagerMainWindowExt()
        self.ui_manager.setupUi(self.manager_window)
        self.manager_window.show()

    def show_material_management(self):
        self.material_window = QMainWindow()
        self.ui_material = MaterialManagementExt()
        self.ui_material.setupUi(self.material_window)
        self.material_window.show()







