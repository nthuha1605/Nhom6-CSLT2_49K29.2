# Trong câu hỏi này, hãy viết một chương trình đảo ngược với câu 41. 
# Bắt đầu bằng cách nhập tần số từ người dùng. 
# Nếu tần số nằm trong phạm vi 1 Hertz của giá trị được liệt kê trong bảng ở câu hỏi trước thì in ra tên của nốt nhạc. 
# Nếu không thì in ra rằng tần số không tương ứng với một nốt đã biết. 
# Trong bài tập này bạn chỉ cần xem xét các ghi chú được liệt kê trong bảng câu 41. 
# Không cần phải xem xét các nốt từ các quãng tám khác.

Hz = float(input('Enter frequency: '))

if 260.63 <= Hz <= 262.63:
    print(Hz, 'Hz is C4 note.')
elif 292.66 <= Hz <= 294.66:
    print(Hz, 'Hz is D4 note.')
elif 328.63 <= Hz <= 330.63:
    print(Hz, 'Hz is E4 note.')
elif 348.23 <= Hz <= 350.23:
    print(Hz, 'Hz is F4 note.')
elif 391.00 <= Hz <= 393.00:
    print(Hz, 'Hz is G4 note.')
elif 439.00 <= Hz <= 441.00:
    print(Hz, 'Hz is A4 note.')
elif 492.88 <= Hz <= 494.88:
    print(Hz, 'Hz is B4 note.')
else:
    print(Hz, 'Hz does not correspond to a known note.')