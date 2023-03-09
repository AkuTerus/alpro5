jumlah_sks = int(input('masukan jumlah sks : '))
matkul = 0
jumlah_nilai = 0 
while matkul<jumlah_sks:
    matkul = matkul+1
    input_nilai = input(f'Nilai matkul {matkul} : ')
    kecil = input_nilai.lower()
    if kecil == 'a':
        jumlah_nilai = jumlah_nilai+4
    elif kecil =='b':
        jumlah_nilai = jumlah_nilai+3
    elif kecil == 'c':
        jumlah_nilai = jumlah_nilai+2
    elif kecil == 'd':
        jumlah_nilai= jumlah_nilai+1
    else:
        print('nilai hanya a b c d')

print(f'nilai anda  {jumlah_nilai/jumlah_sks:.2f}')