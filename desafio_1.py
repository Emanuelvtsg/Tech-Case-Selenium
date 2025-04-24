# inputs exemplo
# [1, 2, 4, 5]
# R: 3
# [1, 5, 8, 6, 10, 2, 4, 9, 3]
# R: 7
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]
# R: 93

input = input()

# converte o input para um array
array_input = eval(input)

# inicializa array auxiliar com 0s, do mesmo tamanho do array input + o item que falta
array_auxiliar = [0] * (len(array_input) + 1)

# povoa array auxiliar, esse array estará ordenado, e, no final, a única posição com 0 será a que está faltando
for i in array_input:
    array_auxiliar[i-1] = i

# itera o array auxiliar para encontrar qual posição faltou
for i in array_auxiliar:
    if i == 0:
        print(array_auxiliar.index(i) + 1)