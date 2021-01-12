from datetime import  *
import os

if (os.path.exists('data pinjaman.txt')) :
    mode = 'a'
else :
    mode = 'w'
buka = open('data pinjaman.txt', mode)

while True :
    # input kode,nama dan judul buku
    kode_member = input('Masukkan Kode Member : ')
    nama_member = input('Masukkan Nama Member : ')
    judul_buku = input('Masukkan Judul Buku : ')
    pinjam_hari = date.today()
    pinjam_kembali = pinjam_hari + timedelta(days = 7 )
    data = [kode_member, nama_member, judul_buku, str(pinjam_hari), str(pinjam_kembali), '\n']
    buka.write('|'.join(data))

    print('')
    ulang = input('Ulangi lagi (y/n) : ')
    print('')
    if (ulang == 'Y') :
        continue
    elif (ulang == 'N') :
        break
    else :
        print('tidak valid')

buka.close()