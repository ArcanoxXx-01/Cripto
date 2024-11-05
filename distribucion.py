import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def tabla_frecuencias_y_distribucion(df, muestra, cantidad_clases,min_valor,max_valor,mostrar_grafica=False):
    
    #Crear los intervalos de clase y calcular las frecuencias
    clases = np.linspace(min_valor, max_valor, cantidad_clases + 1)
    frecuencias, _ = np.histogram(df[muestra], bins=clases)
    
    # Crear el DataFrame de tabla de frecuencias
    tabla_frecuencias = pd.DataFrame({
        'Intervalo': [f'{int(clases[i])} - {int(clases[i+1])}' for i in range(cantidad_clases)],
        'Frecuencia': frecuencias
    })
    
    #Calcular la distribución acumulada
    tabla_frecuencias['Frecuencia Acumulada'] = tabla_frecuencias['Frecuencia'].cumsum()
    tabla_frecuencias['Distribución Acumulada'] = tabla_frecuencias['Frecuencia Acumulada'] / len(df[muestra])
    
    # # Mostrar la tabla de frecuencias
    # print("Tabla de Frecuencias:")
    # print(tabla_frecuencias)
    
    #Graficar la función de distribución
    plt.figure(figsize=(10, 6))
    plt.plot(clases[1:], tabla_frecuencias['Frecuencia'], marker='o', color='b', linestyle='-',label='distribucion')
    plt.plot(clases[1:], tabla_frecuencias['Frecuencia Acumulada'], marker='o', color='red', linestyle='-',label='acumulada')    
    plt.title('Función de Distribución & Distribución Acumulada')
    plt.xlabel('Valor')
    plt.grid(True)
    plt.legend()
    if(mostrar_grafica):
        plt.show()
    return tabla_frecuencias

#Ejemplo de uso:

path = '/home/arcanox/Escritorio/proyectos/Estadistica/db/BTCUSD_d.csv'
# tamaño de la muestra (últimos n dias)
n=3500 
# limites del rango a analisar
min_valor = 0 ; max_valor = 100000 
# dato del data frame que se quiere analisar
muestra='open' 
# crear el dataframe usando los ultimos n dias
df=pd.read_csv(path, nrows=n)
# indicar si graficar las funciones de distribucion
mostrar = True

tabla_frecuencias_y_distribucion(df,muestra,10,min_valor,max_valor,mostrar)