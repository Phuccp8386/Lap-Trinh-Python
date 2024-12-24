# 4.2.6.	Viết chương trình đếm số lần xuất hiện các kí tự trong xâu cho trước, ví dụ xâu s="nngeunuee1n", kết quả là 'n': 4, 'g':1, 'u':2, 'e' : 3, '1': 1
def dem():
    s = input()
    count1 = {}
    for char in s:
        if char in count1:
            count1[char] += 1 
        else:
            count1[char] = 1
    
    for char, count in count1.items():
        print(f"'{char}': {count}")

dem()
