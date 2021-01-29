"""
Tipe data dictionary sekedar menghubungkan antara Key dan Value
KVP = Key Value Pair
dictionary = kamus
"""
kamus_ind_eng = {'anak': 'son', 'istri': 'wive', 'ayah':'father'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['anak'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}
print(data_dari_server_gojek)
print(f"\nList Driver{data_dari_server_gojek['driver_list']}")
print(f"\nNama Driver: {data_dari_server_gojek['driver_list'][0]}")
print(f"\nNama Driver: {data_dari_server_gojek['driver_list'][0]['nama']} "
      f"berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")