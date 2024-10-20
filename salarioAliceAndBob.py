# Definição dos salários
salario_alice = 1000 + 0.2 * 3950
salario_bob = 999 + 0.05 * 20000

# Exibição dos salários individuais
print(f"Salário da Alice: R$ {salario_alice:.2f}")
print(f"Salário do Bob: R$ {salario_bob:.2f}")

# Cálculo dos custos mensais
aluguel = 900
supermercado = 600
outros_gastos = 300
custo_mensal = aluguel + supermercado + outros_gastos

print(f"Custo mensal total: R$ {custo_mensal:.2f}")

# Cálculo do saldo final
salario_final = salario_alice + salario_bob - custo_mensal

# Exibição do resultado
print(f"A quantia que o casal terá após o pagamento das despesas será de: R$ {salario_final:.2f}")