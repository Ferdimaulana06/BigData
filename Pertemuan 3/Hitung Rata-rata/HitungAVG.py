def read_file(file_path):
    # Menambahkan encoding 'utf-8' saat membaca file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

# Fungsi Map untuk menghitung total nilai dan jumlah data
def map_function_average(line):
    score = float(line.strip())  # Mengonversi string menjadi float
    return [("total", (score, 1))]  # Menggunakan 'total' sebagai key tetap

# Fungsi Reduce untuk menghitung rata-rata nilai
def reduce_function_average(mapped_data):
    total_score = 0
    count = 0
    for key, (score, num) in mapped_data:
        total_score += score
        count += num
    average = total_score / count if count > 0 else 0
    return average

# Path ke file CSV
file_path = 'cobanilai.csv'  # Sesuaikan dengan lokasi file CSV

# Membaca data dari file
data_lines = read_file(file_path)

# Menampilkan nilai-nilai yang dibaca dari file
print("Nilai-nilai yang dibaca dari file:")
for line in data_lines:
    print(line.strip())

# Langkah Map: Memetakan setiap baris ke dalam pasangan key-value
mapped_data = []
for line in data_lines:
    mapped_data.extend(map_function_average(line))

# Langkah Reduce: Menghitung rata-rata nilai
average_score = reduce_function_average(mapped_data)

print("\nRata-rata nilai:", average_score)
