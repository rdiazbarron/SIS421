from PIL import Image
import os

def jpg(ORIGEN, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    for filename in os.listdir(ORIGEN):
        if filename.lower().endswith((".png", ".jpeg", ".bmp", ".gif", ".tiff", ".webp", ".jpg", ".jfif")):
            image_path = os.path.join(ORIGEN, filename)
            try:
                img = Image.open(image_path)
                img = img.convert("RGB")  # Convertir a formato RGB antes de guardar como JPG
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_path = os.path.join(output_path, new_filename)
                img.save(new_path, "JPEG")
            except Exception as e:
                print(f"Error processing {image_path}: {e}")
                continue
#C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\mycone\conofinal
# Ruta a tu directorio de imágenes (notar el prefijo r para indicar una cadena raw)
#C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\myplate\second official plate processed 0
ORIGEN = r"C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\myplate\second official plate processed 0"
output_path = r"C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\myplate\second official plate processed 1"

jpg(ORIGEN, output_path)
