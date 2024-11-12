def imposto(renda_anual):
    if renda_anual <= 6000:
        return 0.0
    elif renda_anual <= 37000:
        return 0.15 * (renda_anual - 6000)
    elif renda_anual <= 80000:
        return 4650 + 0.30 * (renda_anual - 37000)
    else:
        return 17550 + 0.37 * (renda_anual - 80000)

# Testando os exemplos fornecidos
print(imposto(5500))   # 0.0
print(imposto(7000))   # 150.0
print(imposto(38000))  # 4950.0
print(imposto(81000))  # 17920.0