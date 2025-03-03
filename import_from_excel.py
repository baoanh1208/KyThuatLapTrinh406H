def import_from_excel(self):
    filename_cate = "../dataset/employee.xlsx"
    filename = "../dataset/material.xlsx"
    imtool = ImportTool()
    self.employees = imtool.import_employee_excel(filename_cate)
    self.materials = imtool.import_material_excel(filename)
    self.show_employee_gui()
    self.show_material_gui()