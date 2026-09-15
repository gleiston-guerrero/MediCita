
# Evidencia visual de contenido real (respaldo del punto B6 / B3)

Estas dos imágenes son la imagen rasterizada extraída directamente de dos de los ocho
PDF de `02_Evidencias/Consentimientos/` (`C_Enfermería.pdf` y `C_Recepcionista.pdf`),
con la anonimización ya aplicada intacta.

Se incluyen como muestra representativa para que cualquiera pueda verificar, sin
depender de una explicación escrita, que el contenido detrás de cada PDF es un
escaneo real de un papel firmado a mano — letra manuscrita distinta en cada
documento, inclinación natural de la hoja, sombras propias de un escaneo — y no una
plantilla generada por computadora.

Cualquiera puede repetir la extracción sobre cualquiera de los 8 originales con:

```python
from pypdf import PdfReader
r = PdfReader("C_Enfermería.pdf")
for img in r.pages[0].images:
    open("salida.png", "wb").write(img.data)
```

Ver la explicación completa de la procedencia en `02_Evidencias/Readme.md`.
