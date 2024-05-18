#NAMA : SALAKHUDIN
#NIM : 222360003
#PRODI : D3 MANAJEMEN INFORMATIKA

import sqlite3

conn = sqlite3.connect('database_buku.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS buku
                 (ISBN VARCHAR(15), Judul VARCHAR(50), Pengarang VARCHAR(30),
                 Penerbit VARCHAR(30), Kota VARCHAR(25), Tahun VARCHAR(4))''')

def input_data(T):
    buku = 'INSERT INTO buku(ISBN, Judul, Pengarang, Penerbit, Kota, Tahun) VALUES ("'+no+'", "'+judul+'", "'+pengarang+'", "'+penerbit+'", "'+kota+'", "'+tahun+'")'
    tambah = conn.execute(buku)
    return tambah

def tampil(L):
    tampilkan = '''SELECT * FROM buku'''
    hasil = conn.execute(tampilkan).fetchall()
    for baris in hasil:
        print(hasil)
    return hasil

while True:
    print("Selamat datang, silahkan pilih proses yang ingin dilakukan:")
    print("[T]ambah data / [L]ihat data / [K]eluar program")
    print(" ")
    main = input("Pilihan: ").capitalize()
    if main == "T":
        try:
            no = input("ISBN: ")
            judul = input("Judul Buku: ")
            pengarang = input("Pengarang: ")
            penerbit = input("Penerbit: ")
            kota = input("Kota: ")
            tahun = input("Tahun: ")
        except:
            print("Masukan Input")
        input_data("T")
        simpan = input("Simpan?Y/T : (bila Y maka data disimpan,bila T maka data tidak disimpan) ").capitalize()
        if simpan == "Y":
            conn.commit()
        else:
            c.close()
    elif main == "L":
        tampil("L")
    elif main == "K":
        quit()
   