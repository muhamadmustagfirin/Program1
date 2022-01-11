print("INPUT NILAI") 
siswa = Mahasiswa() 
siswa.nim = (int(input("masukkan nim : "))) 
siswa.nama = (input("masukkan nama siswa : "))
siswa.tugas = (float(input("Masukkan Nilai Tugas : ")))
siswa.uts = (float(input("Masukkan Nilai UTS : ")))
siswa.uas = (float(input("Masukkan Nilai UAS : ")))
siswa.akhir= siswa.tugas * 0.30 + siswa.uts * 0.35 + siswa.uas * 0.35
dataSiswa[index_update] = siswa
print("Nilai siswa berhasil di input")
