import os
import json
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
print('----------------')
print('----------------')
# Usa barras normales o duplica las barras invertidas en la ruta.
ruta = 'C:/Users/diazb/OneDrive/Escritorio/hid/Inteligencia artificial 2/second exam/modelunet2/train/'

# Carga las anotaciones COCO.
annotations_coco = json.load(open(f'{ruta}_annotations.coco.json', 'r'))

# Obtiene las listas de imágenes y anotaciones.
imagenes = annotations_coco['images']
annotations = annotations_coco['annotations']

# Crea el directorio de máscaras si no existe.
mask_dir = f"{ruta}mask/"
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)

# Procesa cada imagen en el conjunto de datos.
for img in imagenes:
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
