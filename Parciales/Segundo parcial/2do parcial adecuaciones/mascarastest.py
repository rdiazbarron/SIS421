import os
import json
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
print('----------------')
print('----------------')

#generar máscaras a partir de un conjunto de datos de imágenes etiquetadas, 
# donde las anotaciones están en formato JSON siguiendo la especificación de COCO (Common Objects in Context):

ruta = 'C:/Users/diazb/OneDrive/Escritorio/hid/Inteligencia artificial 2/second exam/modelunet2/test/'


annotations_coco = json.load(open(f'{ruta}_annotations.coco.json', 'r'))# Carga las anotaciones COCO.

# Se extraen las listas de imágenes y anotaciones del archivo JSON cargado: 
# Las imágenes contienen metadatos como:    nombre del archivo y el ID de la imagen, 
# mientras que las anotaciones  contienen detalles como :    el ID de la imagen, el ID de la categoría 
# y las coordenadas de segmentación del objeto.

imagenes = annotations_coco['images']# Obtiene las listas de imágenes y anotaciones.
annotations = annotations_coco['annotations']# Obtiene las listas de imágenes y anotaciones.

# Crea el directorio de máscaras si no existe.
mask_dir = f"{ruta}mask/"
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)

# Procesa para cada imagen en el conjunto de datos.
for img in imagenes: #Se extraen las listas de imágenes y anotaciones del archivo JSON cargado. Las imágenes contienen metadatos como el nombre del archivo y el ID de la imagen, mientras que las anotaciones contienen detalles como el ID de la imagen, 
                        #el ID de la categoría y las coordenadas de segmentación del objeto.
    imagen = Image.open(f"{ruta}/{img['file_name']}")
    anns = [a for a in annotations if a['image_id'] == img['id']]
    mask = Image.new('L', (416, 416), 0)
    for ann in anns:
        segmentation = ann['segmentation'][0]
        draw = ImageDraw.Draw(mask)
        draw.polygon(segmentation, outline=ann['category_id'], fill=ann['category_id'])
    
    print(mask.getextrema())
    # Guarda la máscara generada.
    mask.save(f"{mask_dir}{img['file_name'][:-4]}.png")

    # Descomenta las siguientes líneas si quieres visualizar las imágenes y máscaras.
    # plt.imshow(imagen)
    # plt.imshow(mask, cmap='gray', alpha=0.5)
    # plt.show()
