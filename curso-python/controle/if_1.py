nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado? (s/n): ') == 's' else False

# bloco de codigo
if nota >= 9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quradro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota>= 5.5:
    print('Recuperação')
elif nota >= 3.5:
    print('Repcuperação + Trabalho')
else:
    print('Reprovado')


print(nota)