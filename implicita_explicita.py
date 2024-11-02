# Tipagem ímplicita ou Duck typing

def soma(a, b):
    return a + b

resultado1 = soma(5, 3)  # Tipos numéricos (int) - soma numérica
resultado2 = soma("Olá", ", mundo!") # Tipos string (str) - concatenação de strings

print(resultado1) # Output: 8
print(resultado2) # Output: Olá, mundo!

# Tipagem Explícita ou Type Hinting
def saudacao(nome: str, idade:int) -> str:
    idade_str = str(idade)
    
    return f"Olá, {nome}! Você tem {idade_str} anos. {type(idade), type(idade_str)}"

print(saudacao('Alice', 30))