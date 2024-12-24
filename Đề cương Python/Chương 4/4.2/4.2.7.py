# 4.2.7.	Viết chương trình nhập vào từ bàn phím một xâu kí tự. Kiểm tra xem trong xâu có bao nhiêu chữ cái x, với x là một chữ cái nhập từ bàn phím. Hiển thị các kết quả ra màn hình.

def demx():
    s = input()
    x = input()
    count = s.count(x)
    print(f"{x}: {count}")
    
demx()