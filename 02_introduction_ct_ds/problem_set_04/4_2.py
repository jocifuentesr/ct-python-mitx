import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
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
INTERVAL_2 = list(range(2006, 2021))  # Definido para mantener la consistencia con las variables, aunque no se use

# Crear una instancia de la clase Climate
raw_data = Climate('data.csv')

# Generar los datos de temperatura para los años en INTERVAL_1
y = []
for year in INTERVAL_1:
    y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))

# Generar un modelo lineal (grado 1)
models = generate_models(INTERVAL_1, y, [1])

# Evaluar el modelo en los datos de entrenamiento
evaluate_models_on_training(INTERVAL_1, y, models)
