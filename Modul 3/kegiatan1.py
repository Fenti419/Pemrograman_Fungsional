def konversi(j=0):
    def menit(m=0):
        def detik(d=0):
            return ((j * 60 + m) * 60 + d)
        return detik
    return menit

def konversi_waktu(waktu):
    weeks, days, hours, minutes = 0, 0, 0, 0
    if "minggu" in waktu:
        weeks = int(waktu.split(" minggu")[0])
        waktu = waktu.split(" minggu ", 1)[1]
    if "hari" in waktu:
        days = int(waktu.split(" hari")[0])
        waktu = waktu.split(" hari ", 1)[1]
    if "jam" in waktu:
        hours = int(waktu.split(" jam")[0])
        waktu = waktu.split(" jam ", 1)[1]
    if "menit" in waktu:
        minutes = int(waktu.split(" menit")[0])

    total_minutes = weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
    return total_minutes

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

inputData = [konversi_waktu(item) for item in data]
print("inputData =", inputData)
