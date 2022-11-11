from functools import reduce

notas = [6.4, 7.2, 5.8, 8.4]


def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar


notas_finais = map(somar_nota(1.5), notas)
print(notas_finais)


def somar(a, b):
    return a + b


total = reduce(somar, notas, 0)
print(total)

# isso funciona
# for indice, nota in enumerate(notas):
#     notas[indice] = nota + 1.5

# for indice in range(len(notas)):
#     notas[indice] = notas[indice] + 1.5
