def encontrar_duplicados(elementos):
    """
    Cuenta repeticiones y devuelve una lista de elementos que aparecen más de una vez,
    junto con su frecuencia.
    Retorna: lista de tuplas (elemento, frecuencia) ordenadas por aparición
    """
    conteo = {}
    for elem in elementos:
        conteo[elem] = conteo.get(elem, 0) + 1
    
    # Filtrar solo los que se repiten > 1 vez
    duplicados = [(elem, freq) for elem, freq in conteo.items() if freq > 1]
    
    # Ordenar por orden de aparición original (primera aparición)
    orden_aparicion = []
    vistos = set()
    for elem in elementos:
        if elem in conteo and conteo[elem] > 1 and elem not in vistos:
            orden_aparicion.append(elem)
            vistos.add(elem)
    
    # Construir lista final respetando orden de primera aparición
    resultado = [(elem, conteo[elem]) for elem in orden_aparicion]
    
    return resultado


def main():
    print("=== DuplicateFinder - Buscador de Duplicados ===\n")
    
    while True:
        entrada = input("Ingresa los elementos separados por coma (o 'salir'): ").strip()
        
        if entrada.lower() in ['salir', 'exit', 'q']:
            print("¡Hasta luego!")
            break
        
        if not entrada:
            print("Entrada vacía. Intenta de nuevo.\n")
            continue
        
        # Separar por comas y limpiar espacios
        elementos = [x.strip() for x in entrada.split(',') if x.strip()]
        
        if not elementos:
            print("No se ingresaron elementos válidos.\n")
            continue
        
        print("\nElementos ingresados:")
        print(elementos)
        
        duplicados = encontrar_duplicados(elementos)
        
        if duplicados:
            print("\nElementos que se repiten más de una vez:")
            for elem, freq in duplicados:
                print(f"- {elem} → {freq} veces")
        else:
            print("\nNo se encontraron duplicados.")
        
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()
