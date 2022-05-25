print('Chương trình đổi tiền USD sang VND:')
usd = float(input('Nhập vào số tiền USD: '))
s = float(input('Nhập vào tỉ giá: '))
vnd = usd * s
print(f'Số tiền VND sau khi quy đổi: {round(vnd,3)}')