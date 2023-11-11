# Viết chương trình nhập mức âm thanh tính bằng decibel (dB) từ người dùng dựa vào bảng sau:
# Tiếng ồn                | dB
# Jackhammer              | 130
# Gas lawnmower           | 106
# Alarm clock             | 70
# Quiet room              | 70. 
# Nếu mức dB khớp với một trong các tiếng ồn trong bảng thì hiển thị thông báo chỉ chứa tiếng ồn đó. 
# Nếu một số dB giữa các tiếng ồn được liệt kê thì chương trình của bạn sẽ hiển thị một thông báo cho biết mức độ tiếng ồn nằm ở giữa. 
# Đảm bảo tạo đầu ra hợp lý cho giá trị nhỏ hơn tiếng ồn nhỏ nhất & lớn nhất trong bảng.

dB = float(input('Enter dB level: '))

if dB == 130:
    print(dB, 'dB is Jackhammer noise.')
elif dB == 106:
    print(dB, 'dB is Gas lawnmower noise.')
elif dB == 70:
    print(dB, 'dB is Alarm clock noise.')
elif dB == 40:
    print(dB, 'dB is Quiet room noise.')
elif 40 < dB < 70:
    print(dB, 'dB is between Quiet room noise & Alarm clock noise.')
elif 70 < dB < 106:
    print(dB, 'dB is between Alarm clock noise & Gas lawnmower noise.')
elif 106 < dB < 130:
    print(dB, 'dB is between Gas lawnmower noise & Jackhammer noise.')
elif dB < 40:
    print(dB, 'dB is under Quiet room noise.')
else:
    print(dB, 'dB is above Jackhammer noise.')