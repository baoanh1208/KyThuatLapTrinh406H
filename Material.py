class Material:
    def __init__(self,name=None,type=None,supplier=None,import_price=None,import_qty=None,sell_price=None,sold_qty=None,use_day=None):
        self.__name = name  # Tên nguyên liệu
        self.__type = type  # Loại nguyên liệu (Ngắn hạn/Dài hạn)
        self.__supplier = supplier  # Nhà cung cấp
        self.__import_price = import_price  # Giá nhập (VND/kg)
        self.__import_qty = import_qty  # Số lượng nhập trong ngày
        self.__sell_price = sell_price #giá bán
        self.__sold_qty = sold_qty  # Số lượng bán được trong ngày
        self.__use_day = use_day #số ngày sử dụng ước tính
    def __str__(self):
        return f"{self.__name}\t{self.__type}\t{self.__supplier}\t{self.__import_price}\t{self.__sell_price}\t{self.__sold_qty}\T{self.__use_day}"
    def get_name(self):
        return self.__name
    def set_name(self, name: str):
        self.__name = name
    def get_type(self):
        return self.__type
    def set_type(self,type):
        self.__type = type
    def get_supplier(self):
        return self.__supplier
    def set_supplier(self, supplier):
        self.__supplier = supplier
    def get_import_price(self):
        return self.__import_price
    def set_import_price(self, import_price):
        self.__import_price = import_price
    def get_import_qty(self):
        return self.__import_qty
    def set_import_qty(self,import_qty):
        self.__import_qty = import_qty
    def get_sell_price(self):
        return self.__sell_price
    def set_sell_price(self,sell_price):
        self.__sell_price = sell_price
    def get_sold_qty(self):
        return self.__sold_qty
    def set_sold_qty(self, sold_qty):
        self.__sold_qty = sold_qty
    def get_use_day(self):
        return self.__use_day
    def set_use_day(self, use_day):
        self.__use_day = use_day

