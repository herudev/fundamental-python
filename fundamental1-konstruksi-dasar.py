import requests

# try:
#     r = requests.get('https://google.com')
#     print(r.status_code)
#     if r.status_code == 200:
#         print(r.text)
# except Exception as e:
#     print('ada error', e)

# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World!')
print('by Heru')
print('Tanggal 30 Januari 20201')
print('-' * 10)

#PERCABANGAN: Eksekusi terpilih
ingin_cepat=False
if ingin_cepat:
    print('Jalan lurus saja')
else:
    print('Jalan lain')

#PERULANGAN
jumlah_anak=4

for index_anak in range(1,jumlah_anak+1):
    print(f'Halo anak #{index_anak}')
