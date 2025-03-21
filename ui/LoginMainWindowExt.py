from PyQt6.QtWidgets import QMessageBox, QMainWindow, QPushButton, QWidget, QVBoxLayout

from doancuoiky.libs.DataConnector import DataConnector
from doancuoiky.ui.LoginMainWindow import Ui_MainWindow
from doancuoiky.ui.MaterialManagementExt import MaterialManagementExt
from doancuoiky.ui.EmployeeManagementExt import EmployeeManagementExt  # Thêm import cho EmployeeManagement

class ManagerMainWindowExt(QWidget):
    def __init__(self, role):
        super().__init__()
        self.role = role
        self.initUI()
        self.materialWindow = None
        self.employeeWindow = None
        self.materialUI = None
        self.employeeUI = None

    def initUI(self):
        self.setWindowTitle("Quản lý")
        self.setGeometry(200, 200, 400, 200)  # Tăng kích thước cửa sổ quản lý
        self.layout = QVBoxLayout()

        self.btnMaterialManagement = QPushButton("Quản lý nguyên liệu")
        self.btnEmployeeManagement = QPushButton("Quản lý nhân viên")

        self.btnMaterialManagement.clicked.connect(self.openMaterialManagement)
        self.btnEmployeeManagement.clicked.connect(self.openEmployeeManagement)

        self.layout.addWidget(self.btnMaterialManagement)
        self.layout.addWidget(self.btnEmployeeManagement)
        self.setLayout(self.layout)

    def openMaterialManagement(self):
        if self.materialWindow is None:
            self.materialWindow = QMainWindow()
            self.materialWindow.setGeometry(100, 100, 800, 600)  # Tăng kích thước cửa sổ
            self.materialUI = MaterialManagementExt(self.role)
            self.materialUI.setupUi(self.materialWindow)
        self.materialWindow.show()

    def openEmployeeManagement(self):
        if self.employeeWindow is None:
            self.employeeWindow = QMainWindow()
            self.employeeWindow.setGeometry(100, 100, 800, 600)  # Tăng kích thước cửa sổ
            self.employeeUI = EmployeeManagementExt(self.role)
            self.employeeUI.setupUi(self.employeeWindow)
        self.employeeWindow.show()

class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButtonExit.clicked.connect(self.process_exit)

    def process_login(self):
        # Hàm kiểm tra thông tin nhập người dùng và xác định vai trò user
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        if not username or not password:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ username và password!")
            return

        # Xác định vai trò từ radio button
        if self.radioButtonEmployee.isChecked():
            role = "Employee"
        elif self.radioButtonManager.isChecked():
            role = "Manager"
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn vai trò!")
            return

        # Kết nối database
        dc = DataConnector()
        user = dc.login(username, password, role)  # Truy vấn user theo role => thực hiện login

        # Nếu đăng nhập thành công
        if user:
            self.MainWindow.hide()  # Ẩn cửa sổ đăng nhập thay vì đóng

            if role == "Manager":
                self.mainwindow = ManagerMainWindowExt(role)  # Hiển thị cửa sổ quản lý có 2 nút
            else:
                self.mainwindow = QMainWindow()
                self.mainwindow.setGeometry(100, 100, 800, 600)  # Tăng kích thước cửa sổ
                self.myui = EmployeeManagementExt(role)
                self.myui.setupUi(self.mainwindow)
                self.mainwindow.show()

            self.mainwindow.show()
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def process_exit(self):
        # Button exit
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Chắc chắn thoát?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()
