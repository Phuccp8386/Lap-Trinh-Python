class Sv:
    def __init__(self):
        pass
    def nhap(self):
        self.ten, self.masv, self.dtoan, self.dtriet, self.dltc = input().split()
        self.masv = int(self.masv)
        self.dtoan = float(self.dtoan)
        self.dtriet = float(self.dtriet)
        self.dltc = float(self.dltc)
    def tb(self):
        return (self.dtoan + self.dtriet + self.dltc)/3
    def xuat(self):
        print("{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format( self.masv, self.ten, self.dtoan, self.dtriet, self.dltc, self.tb()))
n = int(input())
SV = []
for i in range(n):
    sinhvien = Sv()
    sinhvien.nhap()
    SV.append(sinhvien)
print("Danh sach sinh vien hoc lai")
s = 0
for i in SV:
    d = 0
    if i.dtoan < 4.0:
        d +=1 
    if i.dtriet < 4.0:
        d +=1 
    if i.dltc <4.0:
        d +=1 
    if d >=2:
        i.xuat()
        s +=1
print("Danh sach nay co {0} sinh vien phai hoc lai".format(s))