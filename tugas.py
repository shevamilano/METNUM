def gauss_jordan(matrix):
    n = len(matrix)

    for i in range(n):
        # Mencari baris dengan elemen maksimum pada kolom ke-i
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        # Menukar baris maksimum dengan baris ke-i
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Membuat elemen diagonal menjadi 1
        divisor = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= divisor

        # Menggunakan eliminasi Gauss untuk membuat kolom lain menjadi 0
        for j in range(n):
            if i != j:
                factor = matrix[j][i]
                for k in range(i, n + 1):
                    matrix[j][k] -= factor * matrix[i][k]

    # Mengembalikan hasil
    return [row[n] for row in matrix]


# Sistem persamaan dalam bentuk matriks augmented
matrix = [
    [2, 3, -1, 5],
    [4, 4, -3, 3],
    [-2, 3, -1, 1]
]

# Menyelesaikan sistem persamaan menggunakan metode Gauss-Jordan
solution = gauss_jordan(matrix)

# Menampilkan solusi
print("Solusi:")
for i, sol in enumerate(solution):
    print(f"x{i+1} = {sol}")