# Analizador-educativo-
# Analizador educativo de archivos

Librería en Python que analiza archivos sin ejecutarlos.

## Funciones
- Obtener nombre, extensión y tamaño.
- Calcular el hash SHA-256.
- Buscar indicadores de texto y evaluar el riesgo.
- Exportar los resultados a un reporte TXT.

## Organización
- libreria/archivos.py: información del archivo y hash.
- libreria/deteccion.py: búsqueda de indicadores y riesgo.
- main.py: utiliza las funciones de la librería.

## Uso
Requiere Python 3, sin instalar dependencias externas.

Descarga y extrae el proyecto. Abre una terminal dentro de
la carpeta y ejecuta:

```console
python main.py
```

Cuando solicite la ruta, escribe `prueba.txt`.

Si ya existe `reporte.txt`, renómbralo antes de ejecutar
el análisis para permitir que se genere uno nuevo.

## Aviso
Es una herramienta educativa. Encontrar indicadores no
demuestra que exista malware.
