import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from K24406H.DoAnCuoiKy.libs.DataConnector import DataConnector
from K24406H.DoAnCuoiKy.libs.Tool import Tool
from K24406H.DoAnCuoiKy.ui.EmployeeManagement import Ui_mainWindow

class EmployeeManagementExt(Ui_mainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.employees = self.dc.get_all_employees()
        self.selected_employee = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.hienthi_nhanvien_len_giaodien()
        self.hienthi_nhanvien_len_giaodien()

    def setupSignalandSlot(self):
        self.pushButtonSave.clicked.connect(self.xuly_luu)
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def hienthi_nhanvien_len_giaodien(self, employees=None):
        self.clearLayout(self.verticalLayoutButton)
        if employees is None:
            employees = self.employees
        for emp in employees:
            btn = QPushButton(text=str(emp))
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet, emp))

    def xem_chi_tiet(self, emp):
        self.lineEditEmpId.setText(str(emp['id']))
        self.lineEditEmpName.setText(emp['name'])
        self.lineEditUserName.setText(emp['username'])
        self.lineEditPassWord.setText(emp['password'])
        self.lineEditPosition.setText(emp['position'])
        self.selected_employee = {'id': emp.id, 'name': emp.name, 'username': emp.username, 'password': emp.password, 'position': emp.position}

    def xuly_luu(self):
        emp_id = self.lineEditEmpId.text().strip()
        name = self.lineEditEmpName.text().strip()
        username = self.lineEditUserName.text().strip()
        password = self.lineEditPassWord.text().strip()
        position = self.lineEditPosition.text().strip()

        if not emp_id or not name or not username or not password or not position:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        employee = {'id': emp_id, 'name': name, 'username': username, 'password': password, 'position': position}

        if self.selected_employee and self.selected_employee['id'] == emp_id:
            self.dc.update_employee(employee)
            QMessageBox.information(self.MainWindow, "Thành công", "Cập nhật nhân viên thành công!")
        else:
            self.dc.add_employee(employee)
            QMessageBox.information(self.MainWindow, "Thành công", "Thêm mới nhân viên thành công!")

        self.employees = self.dc.get_all_employees()
        self.hienthi_nhanvien_len_giaodien()

    def xuly_xoa(self):
        if not self.selected_employee:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không có nhân viên được chọn để xóa!")
            return

        reply = QMessageBox.question(
            self.MainWindow, "Xóa nhân viên", "Bạn có chắc muốn xóa nhân viên này?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.dc.delete_employee(self.selected_employee['id'])
            self.employees = self.dc.get_all_employees()
            self.hienthi_nhanvien_len_giaodien()
            QMessageBox.information(self.MainWindow, "Thành công", "Đã xóa nhân viên thành công!")

    def export_to_excel(self):
        filename = '../dataset/employees.xlsx'
        extool = Tool()
        extool.export_employees_to_excel(filename,self.employees)
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def import_from_excel(self):
        filename = "../dataset/employees.xlsx"
        imtool = Tool()
        self.materials = imtool.import_employee_from_excel(filename)
        self.hienthi_nhanvien_len_giaodien()
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã import thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def exit_program(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Bạn có chắc muốn thoát phần mềm không?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()