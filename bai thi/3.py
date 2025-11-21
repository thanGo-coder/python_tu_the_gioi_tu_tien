kg=int(input("nhap can nang cua ban"))
cm=int(input("nhap chieu cao cua ban"))
bmi=kg+cm
if bmi>=25:
    print('thua can')
if bmi>=18.5:
    print('binh thuong')
else:print('gay')