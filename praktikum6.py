print("======>   Indry Widiyani     <======")
print("======>  Program Input Data  <======")
print("======>      TI.22.C1        <======")
data = {}
while True:
    print("")
    m = input(" (L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    print("================================================================")
    print("| NO |  Nama     |   Nim    |  Tugas  |  UTS  |  UAS  |   Akhir |")
    print("================================================================")
    print(">>>>>>>>>>>>>>>>>>>>>>>> TIDAK ADA DATA <<<<<<<<<<<<<<<<<<<<<<<<")
    if m.lower() == 'k':
        break

    elif m.lower() == 'l':
        print("----- DAFTAR NILAI -----")
        print("=" * 83)
        print("| NO |   NAMA     |   NIM        |  TUGAS   |   UTS     |   UAS      |  AKHIR    |")
        print("=" * 83)
        i = 0
        for x in data.items():
            i += 1
            print("|  1 |{0:9}   |{1:9}     |{2:9} |{3:9}  |{4:9}   |{5:9}  |".format(x[0], x[1][0],
                                                                                      x[1][1], x[1][2], x[1][3],
                                                                                      x[1][4], i))

        else:
            print("====================>>>>>>>>>>>>> Tidak Ada Data <<<<<<<<<<<<<====================")

    elif m.lower() == 't':
        print("--------------- Tambah Data ---------------")
        nama = input("Nama                  : ")
        nim = input("Nim                   : ")
        tugas = float(input("Masukan Nilai Tugas   : "))
        uts = float(input("Masukan Nilai UTS     : "))
        uas = float(input("Masukan Nilai UAS     : "))
        akhir = (int(tugas) * .30) + (int(uts) * .35) + (int(uas) * .35)
        data[nama] = nim, tugas, uts, uas, akhir

    elif m.lower() == 'u':
        print("----- Ubah Data Mahasiswa -----")
        nama = input("Nama  : ")
        if nama in data.keys():
            nim = input("Nim : ")
            tugas = float(input("masukan nilai tugas : "))
            uts = float(input("masukan nilai Uts : "))
            uas = float(input("masukan nilai uas : "))
            akhir = (int(tugas) * .30) + (int(uts) * .35) + (int(uas) * .35)
            data[nama] = nim, tugas, uts, uas, akhir

        else:
            print("Tidak Ada data")

    elif m.lower() == 'h':
        print("Hapus Data Mahasiswa")
        nama = input("nama : ")
        if nama in data.keys():
            print("Datanya", nama, "adalah {0}".format(data[nama]))
        else:
            print("Tidaak Ada Data")

    elif m.lower() == 'c':
        print("Cari Data")
        nama = input("Masukkan Nama : ")
        if nama in data.keys():
            print("Data Telah Di Temukan")
            print("=" * 73)
            print("|                             Daftar Mahasiswa                          |")
            print("=" * 73)
            print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("=" * 73)
            print("| {0:9} | {1:9} | {2:9} | {3:9} | {4:9} | {5:9} |"
                  .format(nama, nim, uts, uas, tugas, akhir))

            print("=" * 73)
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

    else:
        print("Pilih menu yang tersedia")