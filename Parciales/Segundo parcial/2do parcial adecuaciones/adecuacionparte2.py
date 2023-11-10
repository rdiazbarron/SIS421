from PIL import Image
import os

def redimensionar(folder_path, output_folder_path, size=(416, 416)):
    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Recorre todos los archivos en la carpeta
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".png")):
            # Obtiene la ruta completa del archivo de entrada
            input_image_path = os.path.join(folder_path, filename)

            # Obtiene el nuevo nombre del archivo de salida
            output_image_path = os.path.join(output_folder_path, filename)

            try:
                # Abre la imagen utilizando Pillow
                with Image.open(input_image_path) as image:
                    # Redimensiona la imagen al tamaño deseado (512x512 por defecto)
                    resized_image = image.resize(size, Image.ANTIALIAS)

                    # Guarda la imagen redimensionada
                    resized_image.save(output_image_path)

            except Exception as e:
                print(f"Error al procesar {input_image_path}: {e}")


# Define las rutas a tus carpetas de imágenes
dataset_path = r"C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\myplate\second official plate processed 1"
output_path = r"C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\myplate\second official plate processed 2"
# Llama a la función con el tamaño deseado
redimensionar(dataset_path, output_path, size=(416, 416))