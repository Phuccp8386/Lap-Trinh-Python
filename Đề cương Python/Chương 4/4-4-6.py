# Viết chương trình nhập vào một danh sách gồm n sinh viên. In ra màn hình danh sách các sv phải học lại ít nhất 2 môn (sinh viên phải học lại khi điểm < 4.0). Biết thông tin của một sinh viên gồm: tên, mã sv, điểm Toán, điểm Triết, điểm LT C.
# Input: 
# + Dòng thứ nhất nhập vào n là số sinh viên
# + Dòng tiếp theo nhập vào thông tin của các sinh viên theo thứ tự tên, mã, điểm Toán, điểm Triết, điểm LT C.
# Output: 
# + Dòng thứ nhất in ra thông báo "Danh sach sinh vien hoc lai"
# + Các dòng tiếp theo, mỗi dòng in ra thông tin của từng sinh viên theo thứ tự mã sv, tên sv, điểm Toán, điểm Triết, điểm LT C, điểm trung bình. Các thông tin cách nhau dấu cách.
# + Dòng cuối cùng in ra thông báo "Danh sach nay co X sinh vien phai hoc lai"//X là số lượng sv phải học lại ít nhất 2 môn
# Constrains: 1<=n<=200, điểm các môn và điểm trung bình có độ chính xác 2 chữ số thập phân, mã sinh viên là số nguyên dương, tên sinh viên không chứa dấu cách.
# For example:
# Input
# 5
# Huy 87 5.00 3.00 3.00
# Lan 2 3.00 2.00 3.00
# Anh 25 7.00 9.00 10.00
# Van 35 0.00 10.00 9.00
# Trang 76 9.00 9.00 9.00	
# Result
# Danh sach sinh vien hoc lai
# 87 Huy 5.00 3.00 3.00 3.67
# 2 Lan 3.00 2.00 3.00 2.67
# Danh sach nay co 2 sinh vien phai hoc lai
class SinhVien:
    def __init__(self):
        self.Ten = ""
        self.Ma = 0
        self.toan = 0
        self.triet = 0
        self.ltc = 0
        self.dtb = 0
    def nhap(self):
        self.Ten,self.Ma,self.toan,self.triet,self.ltc = input().split()
        self.Ma = int(self.Ma)
        self.toan = float(self.toan)
        self.triet = float(self.triet)
        self.ltc = float(self.ltc)
        self.dtb = (self.toan + self.triet + self.ltc)/3
    def xuat(self):
        dem = 0
        if self.dtb < 4.00:
            print("{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format(self.Ma,self.Ten,self.toan,self.triet,self.ltc,self.dtb))
            dem +=1
    print("Danh sach nay co {0} sinh vien phai hoc lai".format(xuat.dem))
        
n = int(input())
Sv = []
dem  = 0 
for _ in range(n):
    Svien = SinhVien()
    Svien.nhap()
    Svien.xuat()
print("Danh sach sinh vien hoc lai")





