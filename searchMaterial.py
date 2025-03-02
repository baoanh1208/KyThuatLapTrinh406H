def search_material(self):
    """Tìm kiếm nguyên liệu theo tên từ file JSON và hiển thị lên giao diện"""
    material_name = self.__name.text().strip()
    if not material_name:
        QMessageBox.warning(self, "Warning", "Vui lòng nhập tên nguyên liệu để tìm kiếm!")
        return

    # Đảm bảo đọc được file JSON
    with open("dataset/material.json", "r", encoding="utf-8") as file:
        materials = json.load(file)

    for material in materials:
        if material.get("name", "").lower() == material_name.lower():
            # Hiển thị thông tin lên giao diện
            self.__name.setText(material.get('name', ''))
            self.__type.setText(material.get('type', ''))
            self.__supplier.setText(material.get('supplier', ''))
            self.__import_price.setText(str(material.get('import_price', '')))
            self.__import_qty.setText(str(material.get('import_qty', '')))
            self.__sell_price.setText(str(material.get('sell_price', '')))
            self.__sold_qty.setText(str(material.get('sold_qty', '')))
            self.__use_day.setText(str(material.get('use_day', '')))
            return

    QMessageBox.warning(self, "Error", "Không tìm thấy tên nguyên liệu!")
