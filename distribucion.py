import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def tabla_frecuencias_y_distribucion(df, muestra, cantidad_clases):
    # Paso 1: Calcular el rango de cada clase
    max_valor = 100000
    min_valor = 0
    intervalo = (max_valor - min_valor) / cantidad_clases
    
    # Paso 2: Crear los intervalos de clase y calcular las frecuencias
    clases = np.linspace(min_valor, max_valor, cantidad_clases + 1)
    frecuencias, _ = np.histogram(df[muestra], bins=clases)
    
    # Crear el DataFrame de tabla de frecuencias
    tabla_frecuencias = pd.DataFrame({
        'Intervalo': [f'{int(clases[i])} - {int(clases[i+1])}' for i in range(cantidad_clases)],
        'Frecuencia': frecuencias
    })
    
    # Paso 3: Calcular la distribución acumulada
    tabla_frecuencias['Frecuencia Acumulada'] = tabla_frecuencias['Frecuencia'].cumsum()
    tabla_frecuencias['Distribución Acumulada'] = tabla_frecuencias['Frecuencia Acumulada'] / len(df[muestra])
    
    # Mostrar la tabla de frecuencias
    print("Tabla de Frecuencias:")
    print(tabla_frecuencias)
    
    # Paso 4: Graficar la función de distribución acumulada
    plt.figure(figsize=(10, 6))
    plt.plot(clases[1:], tabla_frecuencias['Frecuencia'], marker='o', color='b', linestyle='-')
    plt.title('Función de Distribución')
    plt.xlabel('Valor')
    plt.ylabel('Distribución Acumulada')
    plt.grid(True)
    plt.show()

path = '/home/arcanox/Escritorio/proyectos/Estadistica/db/BTCUSD_d.csv'
n=1000
lector=pd.read_csv(path, nrows=n)
tabla_frecuencias_y_distribucion(lector,'open',10)