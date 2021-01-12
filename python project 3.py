from datetime import*
import os
#membuka file teks data peminjam buku
buka = open('data pinjaman', 'r')
baca = buka.readlines()

kode_member = input('Masukkan Kode Member : ')

for x in range(len(isiTeks)) :
    if (kode_member in isiTeks[x]) :
        splited = isiTeks[x].split('|')
        statusBuku = 'ada'
        break
    
    else :
        statusBuku = 'tidak ada'
        continue

if (statusBuku == 'ada'):
    print("Data Peminjam Buku")
    print("Kode Member   : ", splited [0])
    print("Nama Member  : ", splited [1])
    print("Judul Buku          : ", splited [2])
    print("Tanggal Mulai Peminjaman         : ", splited [3])
    print("Tangal Pengambilan Maksimal    : ", splited [4])
    print("Tanggal Pengembalian Buku        : ", datetime.date(datetime.now()))

    telatPengembalian = Program1. diffDate(splited [4])
    dendaTelat = 2000 * abs(telatPengembalian)

    if(telatPengembalian >= 0 ) :
        print('Terlambat : 0 hari')
        print('Denda       : 0')
    else :
        print('Terlambat : ', abs(telatPengembalian))
        print('Denda       : ', dendaTelat)
else :
    print('Peminjaman Buku Tidak Ada')