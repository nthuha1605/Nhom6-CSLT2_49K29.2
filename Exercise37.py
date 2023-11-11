'''
Viết chương trình xác định tên của một hình dựa vào số cạnh của nó. Đọc số mặt của người dùng và sau đó báo 
cáo tên thích hợp như một phần của một thông điệp ý nghĩa. Chương trình của bạn phải hỗ trợ các hình dạng 
có kích thước từ 3 lên đến (và bao gồm) 10 mặt. Nếu nhập vào một số cạnh ngoài phạm vi này thì chương trình
của bạn sẽ hiển thị thông báo lỗi thích hợp.
'''
num=int(input('Enter the number of edges: '))
if num==3:
    shape='Triangle'
elif num==4:
    shape='Quadrangle'
elif num==5:
    shape='The Pentagon'
elif num==6:
    shape='Hexagon'
elif num==7:
    shape='Heptagon '
elif num==8:
    shape='Octagon '
elif num==9:
    shape='Nonagon '
elif num==10:
    shape='Decagon'
else:
    print('Invalid edge number')
if 3<=num<=10:
    print(shape) 