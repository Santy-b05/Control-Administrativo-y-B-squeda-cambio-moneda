import pandas as pd
import numpy as np

datos = {
    'ID_Venta': [101, 102, 103, 104, 105, 106, 107],
    'Sucursal': [' Buenos Aires ', 'Sao Paulo', 'CDMX', 'BUENOS AIRES', 'sao paulo', ' Cdmx ', 'Buenos Aires'],
    'Moneda': ['ARS', 'BRL', 'MXN', 'ARS', 'BRL', 'MXN', np.nan],
    'Monto_Local': [150000.0, 3200.0, 12000.0, 220000.0, np.nan, 8500.0, 95000.0],
    'Cliente': ['Juan Perez', 'Thiago Silva', 'Carlos Lopez', 'Maria Gomez', 'Ana Souza', 'Sofia Hernandez', 'Diego Diaz']
}

df = pd.DataFrame(datos)
df.to_excel('ventas_internacionales.xlsx', index=False)
print("¡Archivo 'ventas_internacionales.xlsx' generado con éxito!")