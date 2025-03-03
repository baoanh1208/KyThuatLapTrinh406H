def loc_nguyen_lieu(self,type):
    """Lọc nguyên liệu theo loại ngắn hạn hoặc dài hạn."""
    danhsach_nguyenlieu = []
    for mtrs in materials():
        if mtrs.type== type:
            danhsach_nguyenlieu.append(mtrs)
    return danhsach_nguyenlieu

