import random

# Fungsi untuk mengambil input pengguna
def get_user_input():
    feed_data = []
    n = int(input("Masukkan jumlah jenis bahan pakan: "))
    
    for i in range(n):
        nama = input(f"Masukkan nama bahan pakan ke-{i+1}: ")
        protein = float(input(f"Masukkan kandungan protein untuk {nama}: "))
        karbo = float(input(f"Masukkan kandungan karbohidrat untuk {nama}: "))
        lemak = float(input(f"Masukkan kandungan lemak untuk {nama}: "))
        feed_data.append({'nama': nama, 'protein': protein, 'karbo': karbo, 'lemak': lemak})
    
    required_protein = float(input("Masukkan kebutuhan protein: "))
    required_karbo = float(input("Masukkan kebutuhan karbohidrat: "))
    required_lemak = float(input("Masukkan kebutuhan lemak: "))
    
    return feed_data, required_protein, required_karbo, required_lemak

# Fungsi untuk menghitung total nutrisi dari kombinasi bahan pakan
def calculate_nutrition(combination):
    total_protein = sum(feed['protein'] for feed in combination)
    total_karbo = sum(feed['karbo'] for feed in combination)
    total_lemak = sum(feed['lemak'] for feed in combination)
    return total_protein, total_karbo, total_lemak

# Fungsi untuk menghitung skor solusi berdasarkan perbedaan dengan kebutuhan nutrisi
def calculate_score(total_protein, total_karbo, total_lemak, required_protein, required_karbo, required_lemak):
    protein_diff = abs(total_protein - required_protein)
    karbo_diff = abs(total_karbo - required_karbo)
    lemak_diff = abs(total_lemak - required_lemak)
    return protein_diff + karbo_diff + lemak_diff

# Fungsi untuk membangkitkan solusi awal secara acak
def generate_initial_solution(feed_data):
    return random.sample(feed_data, 3)

# Fungsi untuk membangkitkan tetangga dari solusi saat ini
def generate_neighbors(solution, feed_data):
    neighbors = []
    for i in range(len(solution)):
        for feed in feed_data:
            if feed not in solution:
                neighbor = solution[:]
                neighbor[i] = feed
                neighbors.append(neighbor)
    return neighbors

# Algoritma VNS
def vns(feed_data, required_protein, required_karbo, required_lemak):
    current_solution = generate_initial_solution(feed_data)
    current_score = calculate_score(*calculate_nutrition(current_solution), required_protein, required_karbo, required_lemak)
    print(f"Iterasi 0: Solusi awal = {[feed['nama'] for feed in current_solution]}, Skor solusi = {current_score}")
    
    iteration = 1
    while True:
        neighbors = generate_neighbors(current_solution, feed_data)
        best_neighbor = min(neighbors, key=lambda neighbor: calculate_score(*calculate_nutrition(neighbor), required_protein, required_karbo, required_lemak))
        best_score = calculate_score(*calculate_nutrition(best_neighbor), required_protein, required_karbo, required_lemak)
        
        if best_score < current_score:
            current_solution = best_neighbor
            current_score = best_score
            print(f"Iterasi {iteration}: Solusi terbaik saat ini = {[feed['nama'] for feed in current_solution]}, Skor solusi = {current_score}")
            iteration += 1
        else:
            break
    
    return current_solution, current_score

# Ambil input dari pengguna
feed_data, required_protein, required_karbo, required_lemak = get_user_input()

# Jalankan algoritma VNS
solution, score = vns(feed_data, required_protein, required_karbo, required_lemak)

print("\nSolusi terbaik:")
for feed in solution:
    print(f"{feed['nama']} - Protein: {feed['protein']}, Karbohidrat: {feed['karbo']}, Lemak: {feed['lemak']}")
print(f"Skor solusi: {score}")