def soma(a, b):
    return a+b


somar = soma
print(somar(3, 4))


def operacao_aritimetica(funcao, operador1, operador2):
    return funcao(operador1, operador2)


resultado = operacao_aritimetica(soma, 13, 48)
print(resultado)


def soma_parcial(a):
    # processamento pesado 1 - 10s
    # processamento pesado 2 - 20s
    # processamento pesado 3 - 10s
    def concluir_soma(b):
        return a+b  # - 10s
    return concluir_soma

# aqui ele faz o precesso repetidamente, demorando mais tempo se fosse uma unica função
# soma_total(1,2) - 1m10s
# soma_total(1,3) - 1m10s
# total de tempo gasto 2m20s

# aqui ele ja tem gravado o processamento pesado, fazendo custar menos tempo de execução
# soma_1 = soma_parcial(1) - 1m
# r1 = soma_1(2) - 10s
# r2 = soma_1(3) - 10S
# total de tempo gasto 1m20s


resultado_final = soma_parcial(10)(12)
print(resultado_final)
