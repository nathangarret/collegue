import matplotlib.pyplot as mat_plt

# Entre com dados em: []
x = [31, 43, 55, 67, 79]
y = [22, 34, 46, 58, 70]

# Cria o gráfico
mat_plt.plot(x, y, label="Linha de exemplo", color='blue', marker='o')

# Personaliza
mat_plt.title("Desmontrando a biblioteca: Matplotlib")
mat_plt.xlabel("Eixo x")
mat_plt.ylabel("Eixo y")

# "Print" gráfico
mat_plt.show()