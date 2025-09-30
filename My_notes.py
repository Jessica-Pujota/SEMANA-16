# -*- coding: utf-8 -*-
# Este script realiza la escritura y posterior lectura de un archivo de texto.

# Definición del nombre del archivo
file_name = "my_notes.txt"

# --- 1. Escritura de Archivo de Texto ---
# Usamos 'with open' para asegurar que el archivo se cierre automáticamente
# después de que el bloque de código termine, incluso si hay errores (Cierre de Archivos).
print(f"--- 1. Escribiendo contenido en '{file_name}' ---")

try:
    # El modo 'w' (write) abre el archivo para escritura. Si el archivo existe, borra su contenido.
    with open(file_name, 'w', encoding='utf-8') as file:

        # Usamos el método write() para añadir las notas personales.
        # Es crucial añadir '\n' manualmente para el salto de línea.
        file.write("Nota 1: Revisar el plan de proyecto de la semana.\n")
        file.write("Nota 2: Llamar a Pedro para confirmar la reunión del jueves.\n")
        file.write("Nota 3: Practicar mis habilidades de Python con manejo de archivos.\n")
        file.write("Nota 4: Comprar pilas para el control remoto.\n")

    print(f" Escritura completada. Se han guardado las notas en '{file_name}'.")

except IOError as e:
    # Manejo de errores en caso de problemas de permisos o disco.
    print(f" Error al escribir en el archivo: {e}")

# --- 2. Lectura de Archivo de Texto (Línea por Línea) ---
print("\n--- 2. Leyendo el contenido de vuelta (línea por línea) ---")

try:
    # El modo 'r' (read) abre el archivo para lectura.
    with open(file_name, 'r', encoding='utf-8') as file:
        line_count = 1

        # Usamos un bucle 'while True' y el método readline() para leer el archivo
        # línea por línea hasta el final.
        while True:
            # Lee la siguiente línea del archivo.
            line = file.readline()

            # readline() devuelve una cadena vacía ('') cuando llega al final del archivo.
            # Si no hay más contenido, salimos del bucle.
            if not line:
                break

            # Muestra en la consola la línea leída.
            # Usamos strip() para eliminar el carácter de nueva línea ('\n')
            # que readline() incluye, para una impresión limpia.
            print(f"Línea {line_count}: {line.strip()}")
            line_count += 1

    print("\n✅ Lectura completada. El archivo ha sido cerrado.")

except FileNotFoundError:
    print(f" Error: El archivo '{file_name}' no fue encontrado durante la lectura.")
except IOError as e:
    print(f" Error al leer el archivo: {e}")

# --- 3. Cierre de Archivos ---
# El bloque 'with open' gestiona el cierre automático, cumpliendo con la mejor práctica.
print("\n--- 3. Cierre de Archivos ---")
print(
    "Nota: Gracias al uso de 'with open', el archivo se cerró automáticamente sin necesidad de llamar a file.close().")
