def procesar_vuelos(vuelos):
    """Recorre los vuelos y guarda los resultados en un diccionario."""
    resultados = {}
 
    for codigo, datos in vuelos.items():
        pasajeros = datos["pasajeros"]
        precio = datos["precio"]
 
        resultados[codigo] = {
            "pasajeros": pasajeros,
            "precio_original": precio,
            "precio_final": calcular_precio_final(precio),
            "ingreso": calcular_ingreso(pasajeros, precio),
            "baja_ocupacion": pasajeros < 50,
        }
 
    return resultados
 
 
resultados = procesar_vuelos(vuelos)
 

print("--- RESULTADOS POR VUELO ---")
for codigo, info in resultados.items():
    print(f"Vuelo {codigo}:")
    print(f"  Pasajeros: {info['pasajeros']}")
    print(f"  Precio final: {info['precio_final']:.2f}")
    print(f"  Ingreso: {info['ingreso']:.2f}")
    print(f"  Baja ocupación: {'Sí' if info['baja_ocupacion'] else 'No'}")
 
baja_ocupacion = [c for c, info in resultados.items() if info["baja_ocupacion"]]
print("\n--- VUELOS CON BAJA OCUPACIÓN (< 50 pasajeros) ---")
print(baja_ocupacion)
 
print("\n--- CONSULTA DE UN VUELO ---")
print(resultados["AV101"])