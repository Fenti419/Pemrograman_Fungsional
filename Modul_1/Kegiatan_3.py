# Fungsi untuk menghitung nilai mahasiswa
def hitung_nilai_mahasiswa(nama, nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (nilai_tugas + nilai_uts + nilai_uas) / 3
    return {
        "nama": nama,
        "nilai_tugas": nilai_tugas,
        "nilai_uts": nilai_uts,
        "nilai_uas": nilai_uas,
        "nilai_akhir": nilai_akhir
    }

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua_mahasiswa(daftar_mahasiswa):
    nilai_akhir_semua = []
    for mahasiswa in daftar_mahasiswa:
        nilai_mahasiswa = hitung_nilai_mahasiswa(**mahasiswa)
        nilai_akhir_semua.append(nilai_mahasiswa)
    return nilai_akhir_semua

# Contoh data mahasiswa
mahasiswa1 = {"nama": "Mahasiswa Fenti", "nilai_tugas": 80, "nilai_uts": 75, "nilai_uas": 90}
mahasiswa2 = {"nama": "Mahasiswa Karina", "nilai_tugas": 90, "nilai_uts": 85, "nilai_uas": 88}
mahasiswa3 = {"nama": "Mahasiswa Agustin", "nilai_tugas": 70, "nilai_uts": 60, "nilai_uas": 75}

# Daftar mahasiswa
daftar_mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3]

# Menghitung nilai akhir semua mahasiswa
nilai_akhir_semua = hitung_nilai_akhir_semua_mahasiswa(daftar_mahasiswa)

# Menampilkan nilai akhir semua mahasiswa
for nilai_mahasiswa in nilai_akhir_semua:
    print(f"Nama: {nilai_mahasiswa['nama']}")
    print(f"Nilai Akhir: {nilai_mahasiswa['nilai_akhir']:.2f}")
    print()
