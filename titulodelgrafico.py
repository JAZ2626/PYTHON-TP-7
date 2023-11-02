import matplotlib.pyplot as plt

def crear_grafico_barras(data, titulo, nombre_grafico):
    # Crear el gráfico de barras
    plt.bar(data.index, data.values)

    # Personalizar el gráfico
    plt.xlabel('Etiquetas')
    plt.ylabel('Valores')
    plt.title(titulo)

    # Guardar el gráfico como imagen
    plt.savefig(nombre_grafico + '.png')

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
import pandas as pd

# Crear un dataframe de ejemplo
data = pd.DataFrame({'Etiquetas': ['A', 'B', 'C', 'D'],
                     'Valores': [10, 20, 15, 25]})

# Llamar a la función para crear el gráfico de barras
crear_grafico_barras(data['Valores'], 'Grupo5 Gráfico de Barras', 'grafico_barras')
