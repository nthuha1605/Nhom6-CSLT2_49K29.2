# Tạo một chương trình đọc một chữ cái trong bảng chữ cái.
# Nếu người dùng nhập a, e, i, o hoặc u thì hiển thị thông báo là nguyên âm. 
# Nếu người dùng nhập y thì hiển thị thông báo cho biết y là nguyên âm và đôi khi y là phụ âm. 
# Nếu không, sẽ hiển thị thông báo cho biết chữ cái đó là phụ âm.

letter = input('Enter letter: ')

if letter in 'aeiou':
    print(letter, 'is a vowel.')
elif letter == 'y':
    print(letter, 'is a vowel, and sometimes,', letter, 'is a consonant.')
else:
    print(letter, 'is a consonant.')