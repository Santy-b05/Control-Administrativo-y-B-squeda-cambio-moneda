# 📊 Automatizador de Reportes Financieros y Conversión de Divisas

Script en Python diseñado para automatizar el procesamiento de datos de ventas locales, integrarse con una API de tasas de cambio en tiempo real y generar un reporte ejecutivo en Excel con múltiples hojas (`openpyxl`).

---

## 🚀 Características Principales

* **Consumo de API REST:** Obtiene tasas de cambio actualizadas contra el Dólar (USD) utilizando [ExchangeRate-API](https://www.exchangerate-api.com/).
* **Limpieza y Transformación de Datos:** 
  * Eliminación de registros nulos en campos críticos (`Monto_Local`, `Moneda`).
  * Normalización de textos (capitalización y remoción de espacios innecesarios en la columna `Sucursal`).
* **Conversión de Moneda:** Cálculo automático del equivalente en USD según la tasa correspondiente y redondeo a dos decimales.
* **Agregación y Resumen:** Generación de métricas clave por sucursal (cantidad de ventas, total facturado y promedio de ventas).
* **Exportación Profesional a Excel:** Creación de un reporte optimizado en formato `.xlsx` con hojas separadas para el detalle general y el resumen global.
* **Manejo de Errores:** Validación interactiva de archivos de entrada y control de excepciones (permisos de archivos abiertos, errores de red, etc.).

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **Pandas** (Manipulación y análisis de datos)
* **Requests** (Consumo de la API de tasas de cambio)
* **Openpyxl** (Motor de exportación y manejo de múltiples hojas en Excel)

---

## Instalar dependencias

* pip install -r requirements.txt
* python main.py
