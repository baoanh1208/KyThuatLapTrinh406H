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