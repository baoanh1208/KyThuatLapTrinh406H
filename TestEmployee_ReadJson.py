from K24406H.DoAn.libs.JsonFileFactory import JsonFileFactory
from K24406H.DoAn.models.Employee import Employee

jff=JsonFileFactory()
filename="../dataset/employees.json"
employees=jff.read_data(filename,Employee)
print("Danh sách Employee sau khi đọc file:")
for e in employees:
    print(e)
