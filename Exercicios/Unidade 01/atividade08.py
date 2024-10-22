""" 

Suponha que você já tenha uma lista definida, armazenada em uma váriavel chamada nums, contendo apenas valores numéricos.

Escreva uma expressão que encontre o produto entre o maior valor e o menor valor da lista.

Por exemplo, se a lista for [4, 1, 0.5, 10, 6], a sua expressão encontraria o produto de 0.5 e 10 (=5).

"""
nums = [4, 1, 0.5, 10, 6]

produto = max(nums) * min(nums)
print(produto)