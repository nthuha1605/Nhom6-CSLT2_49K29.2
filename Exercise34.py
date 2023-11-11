# Viết chương trình nhập một số nguyên, in ra hiển thị thông báo cho biết số nguyên là số chẵn hay số lẻ.
n = int(input('n='))
if n % 2 == 0:
    print(n,'is even')
else:
    print(n,'is odd')