from datetime import *
# membuat function  untuk menghitung selisih hari dari tanggal hari ini dengan tanggal x 
def diffDate(x):
    splited = x.split('-')
    hari_list = []
    
    for x in splited :
        hari_list.append(int(x))
    hari = date(hari_list[0], hari_list[1], hari_list[2])
    today = datetime.date(datetime.now())
    kurangi = hari - today
    selisih = abs(kurangi.days)
# mengembalikan (return) bilangan bulat yang merupakan selisih tanggal x dengan tanggal hari ini
    return selisih
