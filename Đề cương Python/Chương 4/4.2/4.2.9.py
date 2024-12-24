# 4.2.9.	Viết chương trình nhập vào 1 chuỗi các số phân cách nhau bởi dấu phẩy, in ra các số lẻ trong danh sách

def timsole():
    s = input()
    so = [int(num) for num in s.split(',')]
    sole = [num for num in so if num % 2 != 0]
    
    print(sole) 

timsole()
