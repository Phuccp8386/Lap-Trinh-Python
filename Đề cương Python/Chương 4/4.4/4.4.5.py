class NV:
    def __init__(self):
        pass
    def nhap(self):
        self.ten, self.ma, self.hsl, self.pc = input().split()
        self.ma = int(self.ma)
        self.hsl = float(self.hsl)
        self.pc = int(self.pc)
    def luong(self):
        return self.hsl *2000000+ self.pc
    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma, self.ten, self.hsl, self.pc, self.luong()))
n = int(input())
ds = []
for i in range(n):
    danh_sach = NV()
    danh_sach.nhap()
    ds.append(danh_sach)
ds.sort(key=lambda x: x.luong(), reverse = True)
print("Danh sach nhan vien da sap xep: {0}".format(n))
for i in ds:
    i.xuat()
    