from PIL import Image
import os

def rename_images(input_path, output_path, start_index=1):
    # Verifica si el directorio de salida existe, si no, créalo
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Enumera los archivos en el directorio de entrada
    for idx, filename in enumerate(os.listdir(input_path)):
        # Verifica si el archivo es una imagen JPG
        if filename.lower().endswith(('.jpg')):
            # Abre la imagen usando Pillow
            with Image.open(os.path.join(input_path, filename)) as img:
                # Construye el nuevo nombre del archivo
                new_filename = f"imagemoreimages{idx + start_index}.png"
                # Guarda la imagen como PNG en el directorio de salida
                img.save(os.path.join(output_path, new_filename), format='PNG')
                #print(f"Renombrando {filename} a {new_filename}")

dataset_path = r"C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\myplate\second official plate processed 2"
output_path = r"C:\Users\diazb\OneDrive\Escritorio\hid\Inteligencia artificial 2\second exam\myplate\second official plate processed 3"
rename_images(dataset_path, output_path, start_index=1)