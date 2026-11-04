from libreria.archivos import informacion, calcular_hash
from libreria.deteccion import buscar_indicadores, evaluar_riesgo


def analizar(ruta):
    try:
        nombre, extension, tamano = informacion(ruta)
        huella = calcular_hash(ruta)
        indicadores, puntos = buscar_indicadores(ruta)
        riesgo = evaluar_riesgo(puntos)

        reporte = (
            f"Archivo: {nombre}\n"
            f"Extensión: {extension or 'Sin extensión'}\n"
            f"Tamaño: {tamano} bytes\n"
            f"SHA-256: {huella}\n"
            f"Indicadores: {', '.join(indicadores) or 'Ninguno'}\n"
            f"Puntuación: {puntos}\n"
            f"Riesgo: {riesgo}\n"
            "Reglas: bajo 0–2, medio 3–6, alto desde 7.\n"
            "Cada indicador suma una sola vez.\n"
            "Encontrar indicadores no demuestra que exista malware.\n"
            "Un riesgo bajo tampoco garantiza seguridad.\n"
        )

        print(reporte)

        with open("reporte.txt", "x", encoding="utf-8") as archivo:
            archivo.write(reporte)

        print("Reporte guardado en reporte.txt")

    except FileExistsError:
        print("El reporte.txt ya existe. Renómbralo para crear otro.")

    except (OSError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    analizar(input("Ruta del archivo: ").strip())
