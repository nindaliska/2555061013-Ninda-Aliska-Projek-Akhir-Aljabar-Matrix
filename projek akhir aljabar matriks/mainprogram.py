import ninda013

matriks_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriks_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def cetak_matriks(matriks):
    for baris in matriks:
        print(baris)
    print()

print("--- HASIL PENJUMLAHAN MATRIKS ---")
hasil_tambah = ninda013.tambah_matriks(matriks_A, matriks_B)
cetak_matriks(hasil_tambah)

print("--- HASIL PENGURANGAN MATRIKS ---")
hasil_kurang = ninda013.kurang_matriks(matriks_A, matriks_B)
cetak_matriks(hasil_kurang)

print("--- HASIL PERKALIAN MATRIKS ---")
hasil_kali = ninda013.kali_matriks(matriks_A, matriks_B)
cetak_matriks(hasil_kali)