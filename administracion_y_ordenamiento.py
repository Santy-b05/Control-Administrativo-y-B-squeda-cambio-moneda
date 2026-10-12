import pandas as pd
import requests

def Datos_Api():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url) # No especificamos USD ya que viene por defecto
    r = response.json()
    return r["rates"]

def Obtener_Datos_Excel():
        verificacion = False
        while not verificacion:
            try:   
                nombreArchivo = input("Ingrese el nombre del archivo (Debe ser extensión .xlsx): ")
                Excel_dataframe = pd.read_excel(f"{nombreArchivo}.xlsx")
                verificacion = True
                return Excel_dataframe
            except FileNotFoundError:
                print("Error al buscar el archivo, verifique el nombre.")

def Limpieza_Y_Transformacion_Datos(datos): # Agrega títulos y quita los espacios innecesarios
    datos = datos.dropna(subset= ["Monto_Local", "Moneda"])
    datos["Sucursal"] = datos["Sucursal"].str.title().str.strip()
    return datos

def Cambio_Monedas_Dolar(datos, cambio_USD): # Crea una nueva columna con las tasas de cambio y el valor en dólares
    tasas = datos["Moneda"].map(cambio_USD)
    datos["Monto_USD"] = (datos["Monto_Local"] / tasas).round(2)
    return datos

def Agrupar_Datos(datos): # Arma una nueva página con la suma, la cant. y el promedio de ventas por sucursal
    tabla_resumen = datos.groupby("Sucursal")["Monto_USD"].agg(
        Cant_ventas='count',
        Total_ventas='sum',
        Prom_ventas='mean'
    ).reset_index()
    return tabla_resumen

def Guardar_Reporte(datos, venta_suc): 
        nombre_arch = "reporte_internacional_usd.xlsx"
        try:
            with pd.ExcelWriter(nombre_arch, engine="openpyxl") as writer:
                datos.to_excel(writer, sheet_name="Detalle_USD", index=False)
                venta_suc.to_excel(writer, sheet_name="Resumen_Global", index=False)
        except PermissionError:
            print("Error de permisos: Verifique de no tener el archivo abierto.")
        except Exception as e:
            print(f"Error al exportar el archivo: {e}")

DataFrame_Excel = Obtener_Datos_Excel()
valor_cambio = Datos_Api()
DataFrame_Excel = Limpieza_Y_Transformacion_Datos(DataFrame_Excel)
DataFrame_Excel = Cambio_Monedas_Dolar(DataFrame_Excel, valor_cambio)
DataFrame_Montos_Sucursales = Agrupar_Datos(DataFrame_Excel)
Guardar_Reporte(DataFrame_Excel, DataFrame_Montos_Sucursales)