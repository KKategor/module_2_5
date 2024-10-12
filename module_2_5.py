# Lesson Функции

def get_matrix(n, m, value):
    matrix1 = []
    for i in range(n):
        matrix2 = []
        for j in range(m):
            matrix2.extend([value])
        matrix1.extend([matrix2])
    return matrix1
result1 = (get_matrix(3, 2, 11))
result2 = (get_matrix(4, 3, 17))
result3 = (get_matrix(5, 4, 56))
print(result1)
print(result2)
print(result3)
