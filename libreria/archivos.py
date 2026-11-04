from pathlib import Path
import hashlib


def informacion(ruta):
    archivo = Path(ruta)

    if not archivo.is_file():
        raise ValueError("La ruta no existe o no es un archivo.")

    return archivo.name, archivo.suffix, archivo.stat().st_size


def calcular_hash(ruta):
    with open(ruta, "rb") as archivo:
        return hashlib.sha256(archivo.read()).hexdigest()
