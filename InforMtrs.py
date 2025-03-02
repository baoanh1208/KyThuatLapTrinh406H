class InforMtrs:
    def __init__(self,Name,Supplier,ImportPrice,QuantityImported,SellingPrice,QuantitySold,EditExpectedUsageDays):
        self.Name=Name
        self.Supplier=Supplier
        self.ImportPrice=ImportPrice
        self.QuantityImported=QuantityImported
        self.SellingPrice=SellingPrice
        self.QuantitySold=QuantitySold
        self.EditExpectedUsageDays=EditExpectedUsageDays
    def __str__(self):
        return f"{self.Name}\t{self.Supplier}\t{self.ImportPrice}\t{self.QuantityImported}\t{self.SellingPrice}\t{self.QuantitySold}\t{self.EditExpectedUsageDays}"