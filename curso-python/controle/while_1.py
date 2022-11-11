total = 0
quantidade = 0
nota = 0

while nota != -1:
    nota =  float(input('Informe a notal ou -1 para sair: '))
    if nota != -1:
        quantidade += 1
        total += nota

print(f'A média da turma é: {total / quantidade}')
