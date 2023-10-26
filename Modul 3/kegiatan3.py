# Data float
data_float = (3.1, 2.7, 5.5)

# Fungsi untuk mengubah float menjadi dictionary
def float_to_dict(float_num):
    ratusan = int(float_num)
    puluhan = int((float_num * 10) % 10)
    satuan = int((float_num * 100) % 10)
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

# Menggunakan map() untuk mengubah data float menjadi dictionary
data_int = list(map(float_to_dict, data_float))

# Data String
data_string = ['Hello', 'Python', 'World', 'AI']

# Menggunakan filter() untuk memfilter data string yang hanya mengandung huruf vokal
def is_vowel(char):
    return char in 'aeiouAEIOU'

filtered_data_string = list(filter(lambda word: any(map(is_vowel, word)), data_string))

# Output
print("Data Float:", data_float)
print("Data Int:")
for item in data_int:
    print(item)
print("Data String:", filtered_data_string)
