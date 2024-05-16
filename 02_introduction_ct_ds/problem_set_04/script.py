import os
import numpy as np
import matplotlib.pyplot as plt
from ps4 import Climate

def r_squared(y, estimated):
    y = np.array(y)
    estimated = np.array(estimated)
    mean_y = np.mean(y)
    ss_total = np.sum((y - mean_y) ** 2)
    ss_res = np.sum((y - estimated) ** 2)
    r2 = 1 - (ss_res / ss_total)
    return r2

def generate_models(x, y, degs):
    models = []
    for deg in degs:
        model = np.polyfit(x, y, deg)
        models.append(model)
    return models

def evaluate_models_on_training(x, y, models):
    for model in models:
        estimated = np.polyval(model, x)
        r2 = r_squared(y, estimated)
        
        plt.scatter(x, y, color='blue')
        plt.plot(x, estimated, color='red')
        
        plt.title(f'Model: {np.array2string(model, precision=2, separator=",")}\nR^2: {r2:.3f}')
        plt.xlabel('Year')
        plt.ylabel('Temperature (Celsius)')
        
        plt.show()
        
        # Imprimir el valor de R^2 con tres decimales
        print(f'R^2: {r2:.3f}')

# Intervalo de años de interés
INTERVAL_1 = list(range(1961, 2006))

# Crear una instancia de la clase Climate
raw_data = Climate('data.csv')

# Generar los datos de temperatura para el 10 de enero en Boston
y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))

# Generar un modelo lineal (grado 1)
models = generate_models(x, y, [1])

# Evaluar el modelo en los datos de entrenamiento
evaluate_models_on_training(x, y, models)
