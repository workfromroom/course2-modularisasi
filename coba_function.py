# Program menghitung luas segitiga
print('Menghitung luas segitiga')
alas , tinggi = 9 , 7
luas = alas * tinggi / 2
print(f'alas={alas} dikali tinggi={tinggi} sama dengan luas segitiga={luas}')
print()

# Program menghitung luas segitiga dengan menggunakan function
print('Menghitung luas segitiga dengan function')
def hitung_luas(alas, tinggi):
    luas = alas * tinggi / 2
    return luas
print('luas segitiga=',hitung_luas(9,7))