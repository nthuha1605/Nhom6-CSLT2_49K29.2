


'''
Bảng sau liệt kê một quãng tám của các nốt nhạc, bắt đầu bằng nốt C ở giữa, dọc theo
với tần số của chúng.
Ghi chú   |   Tần số (Hz)
C4        |   261,63
D4        |   293,66
E4        |   329,63
F4        |   349,23
G4        |   392,00
A4        |   440,00
B4        |   493,88



Bắt đầu bằng cách viết một chương trình đọc tên ghi chú từ người dùng và hiển thị tần số của 
nốt nhạc. Chương trình của bạn phải hỗ trợ tất cả các ghi chú được liệt kê trước đó.
Sau khi chương trình của bạn hoạt động chính xác với các ghi chú được liệt kê trước đó, bạn
nên thêm hỗ trợ cho tất cả các nốt từ C0 đến C8. Trong khi điều này có thể được thực hiện bởi
thêm nhiều trường hợp bổ sung vào câu lệnh if của bạn, giải pháp như vậy rất cồng kềnh,
không phù hợp và không thể chấp nhận được vì mục đích của bài tập này. Thay vào đó, bạn nên
khai thác mối quan hệ giữa các nốt trong quãng tám liền kề. Đặc biệt, tần số
của bất kỳ nốt nào trong quãng tám n bằng một nửa tần số của nốt tương ứng trong quãng tám n+1.
Bằng cách sử dụng mối quan hệ này, bạn sẽ có thể thêm hỗ trợ cho các ghi chú bổ sung mà không cần 
thêm các trường hợp bổ sung vào câu lệnh if của bạn.

Gợi ý: Để hoàn thành bài tập này, bạn sẽ cần trích xuất các ký tự riêng lẻ từ tên ghi chú gồm hai 
ký tự để bạn có thể làm việc với chữ cái và số quãng tám riêng biệt. Sau khi đã tách các phần ra, 
hãy tính tần số của nốt trong quãng tám thứ tư bằng cách sử dụng dữ liệu trong bảng trên.
Sau đó chia tần số cho 24-x, trong đó x là số quãng tám được nhập bởi người dùng. Điều này sẽ giảm
một nửa hoặc gấp đôi tần số với số lần chính xác.
'''
text= input('Enter text: ')
num = int(input('Enter number: '))
print('Note the music name: ',text,num,sep='')

if text == 'C':
    Hz = 261.63/(2**(4-num))
elif text == 'D':
    Hz = 293.66/(2**(4-num))
elif text == 'E':
    Hz = 329.63/(2**(4-num))
elif text == 'F':
    Hz = 349.23/(2**(4-num))
elif text == 'G':
    Hz = 392.00/(2**(4-num))
elif text == 'A':
    Hz = 440.00/(2**(4-num))
elif text == 'B'/(2**(4-num)):
    Hz = 493.88
elif text == 'C':
    Hz = 261.63/(2**(4-num))
else:
    print("Invalid note. Please enter a valid note name (e.g., C4, D4, A4, etc).")
print('Frequency :', round(Hz, 2),'Hz')
