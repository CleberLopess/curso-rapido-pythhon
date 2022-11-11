# # repetindo 10x
# for i in range(10):
#     print(i)

# # repetindo de 1 ate 11
# for i in range(1, 11):
#     print(i)

# # repetindo de 1 ate 100 de 7 em 7
# for i in range(1, 100, 7):
#     print(i)

# nums = [2,4,6,8]

# for n in nums:
#     print(n)

# texto =  'Python é muito massa!'

# for letra in texto:
#     print(letra)

produto = {
    'nome': 'Caneta',
    'preco': '8.80',
    'desc': '0.5'
}

for atrib, valor in produto.items(): 
    print(atrib,':', valor)