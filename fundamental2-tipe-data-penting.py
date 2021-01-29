print('Tipe data skalar => tipe data sederhana')
anak1='Dedi'
anak2='Erma'
anak3='Heru'
anak4='Erwin'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTipe data list, disebut juga daftar/array')
anak=['Dedi','Erma','Heru','Erwin']
print(anak)
anak.append('Mantu')
print(anak)

print('\nSapa anak ke-2')
print(f'Hai {anak[1]}')

print('\nSapa semua anak')
for a in range(0,len(anak)):
    print(f'Hai {anak[a]}')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}')

