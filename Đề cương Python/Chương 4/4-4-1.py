# Xây dựng lớp Sách (tên, số trang, giá tiền). 
# Viết các phương thức khởi tạo, nhập, xuất. 
# Viết chương trình nhập vào một mảng n quyển sách, sắp xếp mảng theo chiều giảm dần của giá tiền trung bình của một trang sách và in kết quả vào file sach.txt

class Book:
    def __init__(self):
        self.name = 0
        self.page = 0
        self.cost = 0
        self.average = 0
    def nhap(self):
        self.name = input()
        self.page = int(input())
        self.cost = int(input())
        self.average = round(self.cost/self.page,2)

    def xuat(self):
        print(self.name,self.page,self.cost,self.average)

n = int(input())
books = []
for i in range (n):
    print(f"Nhap quyen sach thu {i+1}: ")
    book = Book()
    book.nhap()
    books.append(book)
    books.sort(key=lambda book: book.average, reverse=True)
for b in books:
    b.xuat()