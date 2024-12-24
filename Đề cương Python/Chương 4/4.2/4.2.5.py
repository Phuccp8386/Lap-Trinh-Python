# 4.2.5.	Viết chương trình nhập một xâu kí tự từ bàn phím. 
# Kiểm tra xem trong xâu có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường, bao nhiêu chữ số. Hiển thị các kết quả ra màn hình

def demkitu():
    s = input()
    count1 = 0
    count2 = 0
    count3 = 0
    for char in s:
        if char.isupper():
            count1 += 1
        if char.islower():
            count2 += 1
        if char.isdigit():
            count3 += 1
    print(count1, count2, count3)
    
demkitu()