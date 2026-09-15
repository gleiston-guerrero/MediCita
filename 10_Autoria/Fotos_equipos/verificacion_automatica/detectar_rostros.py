
"""
Verificacion objetiva y reproducible de que las fotos del equipo en la
organizacion muestran integrantes identificables (rostro visible).

No depende de una apreciacion subjetiva: usa deteccion de rostros por
software (OpenCV, algoritmo Viola-Jones / Haar cascade), el mismo tipo
de deteccion que usan la mayoria de camaras y apps de fotos.

Requisitos: pip install opencv-python-headless
Uso: python3 detectar_rostros.py
"""
import cv2
import os

FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

ARCHIVOS = [
    "../2026_09_04_Facha_Establecimiento.jpg",
    "../2026_09_04_Pasillo_Entrda(principal).jpg",
    "../2026_09_04_Area_Recepción(Recaudación).jpg",
]

def detectar(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    min_size = int(img.shape[0] * 0.06)
    faces = FACE_CASCADE.detectMultiScale(
        gray, scaleFactor=1.08, minNeighbors=7, minSize=(min_size, min_size)
    )
    return img, faces

if __name__ == "__main__":
    os.makedirs("salida", exist_ok=True)
    for path in ARCHIVOS:
        img, faces = detectar(path)
        print(f"{os.path.basename(path)}: {len(faces)} rostro(s) detectado(s)")
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 8)
        out = os.path.join("salida", os.path.basename(path) + "_DETECCION.jpg")
        cv2.imwrite(out, img)
