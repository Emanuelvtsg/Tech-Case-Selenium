# inputs exemplo
# [3, 1, 2, 4, 7, 6, 9, 8]
# R: [2, 4, 6, 8, 3, 1, 7, 9]
# [3, 7, 2, 1, 6, 2, 6, 15, 20, 10, 12, 10, 10, 5, 3, 2, 1]
# R: [2, 6, 2, 6, 20, 10, 12, 10, 10, 2, 3, 7, 1, 15, 5, 3, 1]

input = input()

# converte o input para um array
array_input = eval(input)

# inicializa os arrays destinados a pares e impares
array_par = []

array_impar = []

# itera o array input, se o numero for par, anexa no array par, se for ímpar, anexa no array ímpar
for i in array_input:
    if i%2 == 0:
        array_par.append(i)
    else:
        array_impar.append(i)

# concatena os dois arrays
array_final = array_par + array_impar

print(array_final)
