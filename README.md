# DuplicateFinder

Un buscador de duplicados simple en Python.  
Recibe una lista de elementos (números, strings, etc.), cuenta cuántas veces se repite cada uno y devuelve una lista con los elementos que aparecen **más de una vez** (duplicados).

Ideal para practicar:
- Diccionarios para conteo de frecuencias
- Bucles y condicionales
- Listas y comprensión de listas
- Manejo de entrada/salida


## Requisitos

- Python 3.6 o superior
- No requiere librerías externas

## Instalación

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/camilobaezam/DuplicateFinder.git
   cd DuplicateFinder
## Uso
Ejecuta el programa:
python DuplicateFinder.py
Luego ingresa los elementos separados por comas (pueden ser números o texto).

## Ejemplo de ejecución

=== DuplicateFinder - Buscador de Duplicados ===

Ingresa los elementos separados por coma (o 'salir'): 1,4,6,2,4,3,1,1,3,5,6,7,3,4,5,5,5,3,3,2,1,2,1,1,1,2,6,6

Elementos ingresados:
[1, 4, 6, 2, 4, 3, 1, 1, 3, 5, 6, 7, 3, 4, 5, 5, 5, 3, 3, 2, 1, 2, 1, 1, 1, 2, 6, 6]

Elementos que se repiten más de una vez:
- 1 → 7 veces
- 2 → 4 veces
- 3 → 5 veces
- 4 → 3 veces
- 5 → 4 veces
- 6 → 4 veces

Otro ejemplo:

Ingresa los elementos separados por coma (o 'salir'): hola,mundo,hola,python,hola

Elementos que se repiten más de una vez:
- hola → 3 veces

## Ejemplos adicionales

Lista sin duplicados

Ingresa los elementos separados por coma (o 'salir'): 1,2,3,4,5

→ "No se encontraron duplicados."

Lista vacía o solo Enter

→ "No se ingresaron elementos."

Solo texto

Ingresa los elementos separados por coma (o 'salir'): perro,gato,perro,perro,raton

→ Duplicados: perro (3 veces)

## Notas

- Funciona con números y strings (cualquier tipo hashable)
- No distingue mayúsculas/minúsculas si quieres (puedes agregar .lower() si lo necesitas)
- Muestra los duplicados en orden de aparición en la lista original
- Ignora entradas vacías después del split

## Ideas para extender

- Ordenar duplicados por cantidad de repeticiones
- Mostrar porcentaje de duplicados
- Guardar resultados en archivo
- Permitir cargar desde archivo
- Interfaz gráfica con tkinter
- Detectar duplicados consecutivos o adyacentes

## Autor
Camilo Baeza
