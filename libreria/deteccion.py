def buscar_indicadores(ruta):
    reglas = {
        "os.system": 3,
        "subprocess": 3,
        "powershell": 3,
        "base64": 1,
    }

    with open(ruta, "rb") as archivo:
        contenido = archivo.read().lower()

    encontrados = []
    puntos = 0

    for palabra, valor in reglas.items():
        if palabra.encode() in contenido:
            encontrados.append(palabra)
            puntos += valor

    return encontrados, puntos


def evaluar_riesgo(puntos):
    if puntos >= 7:
        return "alto"
    elif puntos >= 3:
        return "medio"
    else:
        return "bajo"
