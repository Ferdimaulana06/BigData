from collections import defaultdict

# Fungsi untuk membaca file teks
def read_file(file_path):
    with open(file_path, 'r') as file:
        text_data = file.readlines()
    return text_data

# Fungsi untuk memetakan kata menjadi pasangan 
def map_function(text):
    words = text.split()
    mapped = [(word, 1) for word in words]
    return mapped

# Fungsi untuk menggabungkan jumlah kemunculan setiap kata
def reduce_function(mapped_data):
    word_count = defaultdict(int)
    for word, count in mapped_data:
        word_count[word] += count
    return dict(word_count)

# Path ke file teks
file_path = 'BuatDataset.txt'  # Sesuaikan dengan lokasi file txt

# Membaca data dari file
text_data = read_file(file_path)

# Langkah Map: Memetakan setiap kalimat ke dalam pasangan
mapped_data = []
for text in text_data:
    mapped_data.extend(map_function(text))

# Langkah Reduce: Menghitung total kemunculan setiap kata
word_count = reduce_function(mapped_data)

print("Jumlah kata:", word_count)

