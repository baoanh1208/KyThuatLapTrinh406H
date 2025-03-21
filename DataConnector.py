import os
from fileinput import filename
from operator import index

from doancuoiky.libs.JsonFileFactory import JsonFileFactory
from doancuoiky.models.Employee import Employee
from doancuoiky.models.Manager import Manager
from doancuoiky.models.Material import Material


class DataConnector:
    def get_all_materials(self):
        # Lấy tất cả thông tin nguyên liệu
        jff = JsonFileFactory()
        filename = os.path.join(os.path.dirname(__file__), '../dataset/materials.json')
        materials = jff.read_data(filename, Material)
        return materials

    def get_all_employees(self):
        # Lấy tất cả thông tin nhân viên
        jff = JsonFileFactory()
        filename = os.path.join(os.path.dirname(__file__), '../dataset/employees.json')
        employees = jff.read_data(filename, Employee)
        return employees

    def get_all_managers(self):
        # Lấy tất cả thông tin quản lý
        jff = JsonFileFactory()
        filename = os.path.join(os.path.dirname(__file__), '../dataset/managers.json')
        managers = jff.read_data(filename, Employee)  # Sử dụng Employee model vì dữ liệu tương tự
        return managers
    def get_all_users(self):
    #lấy thông tin của quản l và cả nhân viên để tạo hàm log in
        jff = JsonFileFactory()
        managers = jff.read_data("../dataset/managers.json", Manager)
        employees = jff.read_data("../dataset/employees.json", Employee)
        # Gán role
        for manager in managers:
            manager.Role = "Manager"
        for employee in employees:
            employee.Role = "Employee"
        users = managers + employees
        return users
    def login(self, username, password, role=None):
        # Đăng nhập ở màn hình login
        if role == "Employee":
            users = self.get_all_employees()
        elif role == "Manager":
            users = self.get_all_managers()
        else:
            return None

        for user in users:
            if user.UserName == username and user.Password == password:
                return user
        return None

    def find_index_material(self, name):
        # Tìm vị trí của nguyên liệu trong danh sách
        self.materials = self.get_all_materials()
        for i in range(len(self.materials)):
            material = self.materials[i]
            if material.name == name:
                return i
        return -1
    def find_index_employee(self,name):
        #tìm vị trí của nhân vin trong danh sách
        self.employees=self.get_all_employees()
        for i in range(len(self.employees)):
            employee=self.employees[i]
            if employee.name==name:
                return i
        return -1

    def delete_material(self, name):
        # Chức năng xóa nguyên liệu
        index = self.find_index_material(name)
        if index != -1:
            self.materials.pop(index)
            jff = JsonFileFactory()
            filename = "../dataset/materials.json"
            jff.write_data(self.materials, filename)
    def save_update_material(self,current_material):
    #chức năng cập nhật
        index=self.find_index_material(current_material.name)
        if index !=-1:
            self.materials[index]=current_material
            jff = JsonFileFactory()
            filename = "../dataset/materials.json"
            jff.write_data(self.materials, filename)

    def save_new_material(self, material):
        # Chức năng thêm mới nguyên liệu
        materials = self.get_all_materials()
        materials.append(material)
        jff = JsonFileFactory()
        filename = "../dataset/materials.json"
        jff.write_data(materials, filename)

    def save_new_employee(self,employee):
        #chức năng thêm mới nhân viên
        employees=self.get_all_employees()
        employees.append(employee)
        jff=JsonFileFactory()
        filename="../dataset/employees.json"
        jff.write_data(employees,filename)
    def delete_employee(self,name):
        index=self.find_index_employee(name)
        if index!=-1:
            self.employees.pop(index)
            jff=JsonFileFactory()
            filename="../dataset/employees.json"
            jff.write_data(self.employees,filename)
    def save_update_employee(self,current_employee):
    #chức năng cập nhật
        index=self.find_index_employee(current_employee.name)
        if index !=-1:
            self.materials[index]=current_employee
            jff = JsonFileFactory()
            filename = "../dataset/employees.json"
            jff.write_data(self.employees, filename)