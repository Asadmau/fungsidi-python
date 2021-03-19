#membuat function di python
#menghitung luas persegi panjang

print('hello world')

panjang = 4
lebar = 2

luas = panjang * lebar
print('hitung luas persegi panjang : ', luas)

print('hitungan dengan def/ function')
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas
print('luas persegi panjang adalah : ', hitung_luas_persegi_panjang(10, 5))


print('hitung keliling persegi')

sisi = int(input('input sisi :'))
hitung_keliling = sisi * 4

print('hasil keliling adalah : ', hitung_keliling)

# def function keliling persegi

def hitung_keliling(sisi):
    sisi = int(input('input nilai :'))
    hasil = sisi * 4
    return hasil
print(hitung_keliling(4))