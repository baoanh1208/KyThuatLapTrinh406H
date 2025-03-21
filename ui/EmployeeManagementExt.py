import functools
import os
import webbrowser

from PyQt6.QtWidgets import QPushButton, QMessageBox, QMainWindow, QWidget

from doancuoiky.libs.DataConnector import DataConnector
from doancuoiky.libs.Tool import Tool
from doancuoiky.ui.EmployeeManagement import Ui_EmployeeManagement


class EmployeeManagementExt(QWidget,Ui_EmployeeManagement):
    def __init__(self,role):
        super().__init__()
        self.setupUi(self)  # Gọi setup UI trực tiếp vào chính nó
        self.dc = DataConnector()
        self.role = role
        self.materials = self.dc.get_all_materials()
        self.employees = self.dc.get_all_employees()
        self.managers = self.dc.get_all_managers()
        self.selected_employee = None

        self.hienthi_nhanvien_len_giaodien()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.xuly_luu)
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)
        self.pushButtonSearch.clicked.connect(self.xuly_timkiem)
        self.actionExport_To_Excel_File.triggered.connect(self.export_to_excel)
        self.actionImport_from_Excel.triggered.connect(self.import_from_excel)
        self.actionHelp.triggered.connect(self.open_help)
        self.actionAbout.triggered.connect(self.open_about)
        self.actionExit.triggered.connect(self.exit_program)
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
            btn = QPushButton(text=str(emp['name']))
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet, emp))

    def xem_chi_tiet(self, emp):
        self.lineEditEmpId.setText(str(emp['EmId']))
        self.lineEditEmpName.setText(str(emp['EmpName']))
        self.lineEditEmpName_2.setText(str(emp['EmpUserName']))
        self.lineEditEmpName_3.setText(str(emp['EmpPassword']))
        self.lineEditEmpName_4.setText(str(emp['Position']))
        self.selected_employee = emp
    def xuly_clear(self):
        self.lineEditEmpName.clear()
        self.lineEditEmpId.clear()
        self.lineEditEmpName_2.clear()
        self.lineEditEmpName_3.clear()
        self.lineEditEmpName_4.clear()

    def xuly_luu(self):
        emp_id = self.lineEditEmpId.text().strip()
        name = self.lineEditEmpName.text().strip()
        username = self.lineEditEmpName_2.text().strip()
        password = self.lineEditEmpName_3.text().strip()
        position = self.lineEditEmpName_4.text().strip()

        employee = {"id": emp_id, "name": name, "username": username, "password": password, "position": position}

        index = self.dc.find_index_employee(emp_id)
        if index == -1:
            self.dc.save_new_employee(employee)
            QMessageBox.information(self.MainWindow, "Thành công", "Nhân viên đã được thêm mới!")
        else:
            self.dc.save_update_employee(employee)
            QMessageBox.information(self.MainWindow, "Thành công", "Nhân viên đã được cập nhật!")

        self.employees = self.dc.get_all_employees()
        self.hienthi_nhanvien_len_giaodien()
        self.xuly_clear()#sau khi hoàn thành => clear details
    def xuly_xoa(self):
        name = self.lineEditEmpName.text()
        #hiển thị cửa sổ cảnh báo
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setWindowTitle("Xác nhận xóa")
        msgbox.setText(f"Xác nhận xóa [{name}] ?")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.No:#nếu bấm "No"=> quay về
            return
        # Xóa dữ liệu trong file JSON
        self.dc.delete_employee(name)
        # Load lại danh sách nguyên liệu
        self.materials = self.dc.get_all_materials()
        # Cập nhật giao diện
        self.hienthi_nhanvien_len_giaodien()
        self.xuly_clear()
    def xuly_timkiem(self):
        #Tìm kiếm nhân viên theo tên và cập nhật danh sách hiển thị
        employee_name = self.lineEditSearch.text().strip()  # Lấy tên nhập vào
        if not employee_name:
            QMessageBox.warning(self.MainWindow, "Warning", "Vui lòng nhập tên nhân viên để tìm kiếm!")
            return
        # Lọc danh sách nhân viên
        filtered_employees = [mt for mt in self.employees if employee_name.lower() in mt["EmpName"].lower()]
        if filtered_employees:
            self.hienthi_nhanvien_len_giaodien(filtered_employees)  # Hiển thị danh sách tìm kiếm
        else:
            QMessageBox.warning(self.MainWindow, "Error", "Không tìm thấy nhân viên!")
    def export_to_excel(self):
        filename = '../dataset/employees.xlsx'
        extool = Tool()
        extool.export_employee_to_excel(filename, self.employees)
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()
    def import_from_excel(self):
        filename = "../dataset/employees.xlsx"
        imtool = Tool()
        self.employees = imtool.import_employee_from_excel(filename)
        self.hienthi_nhanvien_len_giaodien()
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã import thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()
    def open_help(self):
        file_help = "HELP.pdf"
        current_path = os.getcwd()
        file_help = f"{current_path}/../assets/{file_help}"
        webbrowser.open_new(file_help)
    def open_about(self):
        file_about = "ABOUT.pdf"
        current_path = os.getcwd()
        file_about = f"{current_path}/../assets/{file_about}"
        webbrowser.open_new(file_about)

    def exit_program(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Bạn có chắc muốn thoát phần mềm không?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()