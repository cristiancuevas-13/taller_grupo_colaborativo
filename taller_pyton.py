# ==========================================
# EJERCICIO 1: Cálculo de precio e ingresos

# ==========================================

def calcular_precio_final(precio_original):
    """
    Aplica un 15% de descuento si el precio es mayor a 500.
    """
    if precio_original > 500:
        return precio_original * 0.85            
    return precio_original

def calcular_ingreso_vuelo(pasajeros, precio_original):
    """
    Calcula el precio final con descuento y el ingreso total de un vuelo.
    """
    precio_final = calcular_precio_final(precio_original)
    ingreso_total = pasajeros * precio_final
    return precio_final, ingreso_total

# ==========================================
# PRUEBA
# ==========================================

datos_vuelos = [
    {"codigo": "AV101", "pasajeros": 120, "precio_original": 600},
    {"codigo": "AV102", "pasajeros": 35,  "precio_original": 450},
    {"codigo": "AV103", "pasajeros": 80,  "precio_original": 550},
    {"codigo": "AV104", "pasajeros": 25,  "precio_original": 700},
]