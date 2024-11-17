import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Criando dados para o gráfico
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Criando a figura e o eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Gerando o gráfico de superfície
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Adicionando uma barra de cores
fig.colorbar(surf)

# Exibindo o gráfico
plt.show()