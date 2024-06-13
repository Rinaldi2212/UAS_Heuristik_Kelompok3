import numpy as np
import random

# Definisikan matriks jarak dari gambar
dist_matrix = np.array([
    [0, 6, 3, 6, 2, 2, 2],
    [9, 0, 9, 3, 3, 4, 5],
    [3, 14, 0, 9, 5, 5, 6],
    [9, 3, 12, 0, 5, 6, 8],
    [3, 4, 7, 5, 0, 1, 3],
    [4, 6, 7, 7, 2, 0, 3],
    [2, 7, 6, 7, 2, 2, 0]
])

# Fungsi untuk menghitung total jarak dari rute yang diberikan
def calculate_total_distance(route, dist_matrix):
    distance = 0
    for i in range(len(route)):
        j = (i + 1) % len(route)
        distance += dist_matrix[route[i], route[j]]
    return distance

# Algoritma Variable Neighborhood Search (VNS)
def VNS(dist_matrix, max_iter=1000):
    n = dist_matrix.shape[0]
    current_route = list(range(n))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, dist_matrix)

    route_locations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    initial_route_locations = [route_locations[i] for i in current_route]
    print(f"Rute awal: {initial_route_locations} dengan jarak {current_distance}")

    best_route, best_distance = current_route[:], current_distance

    for iteration in range(max_iter):
        neighborhood_size = 1
        while neighborhood_size < n:
            # Menghasilkan tetangga dengan menukar dua kota
            new_route = current_route[:]
            i, j = random.sample(range(n), 2)
            new_route[i], new_route[j] = new_route[j], new_route[i]
            new_distance = calculate_total_distance(new_route, dist_matrix)

            if new_distance < best_distance:
                best_route, best_distance = new_route, new_distance
                current_route, current_distance = new_route, new_distance
                neighborhood_size = 1
                new_route_locations = [route_locations[k] for k in current_route]
                print(f"Iterasi {iteration}: Rute baru: {new_route_locations} dengan jarak {current_distance}")
            else:
                neighborhood_size += 1

    return best_route, best_distance

# Jalankan algoritma VNS
best_route, best_distance = VNS(dist_matrix)

# Menampilkan hasil
route_locations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
best_route_locations = [route_locations[i] for i in best_route]
print(f"\nRute terbaik: {best_route_locations}")
print(f"Jarak terbaik: {best_distance}")