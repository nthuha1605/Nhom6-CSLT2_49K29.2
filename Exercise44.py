'''
Canada có ba ngày nghỉ quốc gia mà luôn diễn ra vào cùng các ngày hàng năm.

Ngày Lễ                 |Ngày Tháng
Ngày Tết Nguyên Đán     |1 tháng 1
Ngày Canada             |1 tháng 7
Ngày Giáng Sinh         |25 tháng 12


Holiday                 |Date
New year’s day          |January 1
Canada day              |July 1
Christmas day           |December 25

Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.
Canada has two additional national holidays, Good Friday and Labour Day,
whose dates vary from year to year. There are also numerous provincial and
territorial holidays, some of which have fixed dates, and some of which have
variable dates. We will not consider any of these additional holidays in this
exercise.

Hãy viết một chương trình đọc tháng và ngày từ người dùng. Nếu tháng và ngày khớp với một trong các ngày 
lễ đã được liệt kê trước đó thì chương trình của bạn sẽ hiển thị tên của ngày lễ đó. Nếu không khớp, chương 
trình sẽ cho biết rằng tháng và ngày được nhập không tương ứng với một ngày lễ cố định. Canada cũng có hai 
ngày lễ quốc gia khác, Lễ Chúa Giê-su Thương Khó và Lễ Lao Động, mà có ngày diễn ra thay đổi từ năm này sang 
năm khác. Ngoài ra còn có nhiều ngày lễ cấp tỉnh và lãnh thổ, một số có ngày cố định và một số có ngày diễn ra 
biến đổi. Trong bài tập này, chúng ta không xem xét các ngày lễ bổ sung này.
'''
day=int(input('Enter the day: '))
month=input('Enter the month: ')
if day==1 and month=='January':
    print('New year’s day  ')
elif day==1 and month=='July':
    print('Canada day')
elif day==25 and month=='December':
    print('Christmas day ')
else:
    print('Not a holiday')
