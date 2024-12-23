class Book:
    def __init__(self):
        self.name = ""
        self.page = 0
        self.cost = 0
        self.average = 0
    def nhap(self):
        self.name = input()
        self.page = int(input())
        self.cost = int(input())
        self.average = round(self.cost / self.page, 2)
    def xuat(self):
        return f"{self.name} {self.page} {self.cost} {self.average}"
    
n = int(input())
books = []
for i in range(n):
    print("Nhap quyen sach thu", i+1)
    book = Book()
    book.nhap()
    books.append(book)
books.sort(key = lambda x: (x.average, x.name))
with open("sach.txt", "w") as f:
    f.write("Danh sach nhan vien da sap xep:\n")
    for book in books:
        f.write(book.xuat() + "\n")
