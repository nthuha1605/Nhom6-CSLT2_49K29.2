'''
Thường người ta nói rằng một năm của con người tương đương với 7 năm của chó. Tuy nhiên, phép chuyển đổi đơn giản này không thể hiện 
được việc chó đạt độ trưởng thành sau khoảng hai năm. Do đó, một số người tin rằng việc tính toán mỗi trong hai năm đầu của con người 
như là 10.5 năm của chó, và sau đó mỗi năm người tiếp theo được tính là 4 năm của chó sẽ là cách chuyển đổi chính xác hơn.

Dưới đây là một chương trình để thực hiện việc chuyển đổi từ năm người sang năm chó dựa trên mô tả trong đoạn văn của bạn. Chương trình 
này đảm bảo hoạt động chính xác cho cả trường hợp chuyển đổi dưới hai năm người và trên hai năm người, và sẽ hiển thị thông báo lỗi 
thích hợp nếu người dùng nhập một số âm.
'''
people_y=int(input('Enter person year: '))
if people_y<0:
    print("The number of years must be greater than 0")
else:
    if people_y<=2:
        dog_y=people_y*10.5
    else:
        dog_y=2*10.5+(people_y-2)*4
    print("Dog years correspond to ",people_y,' human years: ',dog_y,sep='')