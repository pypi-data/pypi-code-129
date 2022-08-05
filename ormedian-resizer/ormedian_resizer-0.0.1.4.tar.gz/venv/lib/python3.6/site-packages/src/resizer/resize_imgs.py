from PIL import Image
import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def resizer(new_size: tuple,
            image_path: str, new_folder: str,
            quality: int, n_f=True,
            view=True, out_format=''):
    """

    :param view: if True, there would display window showing resized images
    :param new_size: New Image size e.g (224, 224)
    :param image_path: '/path/to/where/images/are
    :param new_folder: '/Specify/new/folder
    :param quality: The quality of the picture resized
    :param args: at the moment you can specify either jpg or png
    :return: New image resized to new_size
    """

    i = 0
    img_dirs = os.listdir(image_path)
    for img in img_dirs:

        new_path = os.path.join(image_path, img)

        if os.path.isfile(new_path):
            imgs = Image.open(new_path)

            f, e = os.path.splitext(new_path)
            Resized_img = imgs.resize(new_size, Image.ANTIALIAS)
            if not n_f:
                if out_format == 'jpg':
                    Resized_img.save(f + '.jpg', 'JPEG', quality=quality)
                else:
                    Resized_img.save(f + '.png', 'PNG', quality=quality)
                if not view:
                    pass
                Resized_img.show(new_folder)
                i += 1
            
            else:
                image_path = Path(image_path)
                n_folder = os.path.join(image_path.parent, new_folder)
                if not os.path.exists(n_folder):
                    os.mkdir(n_folder)

                if out_format == 'jpg':
                    Resized_img.save(f'{n_folder}/{img}', 'JPEG', quality=quality)
                else:
                    Resized_img.save(f + '.png', 'PNG', quality=quality)

                i += 1
                if not view:
                    pass

                image = mpimg.imread(f'{n_folder}/{img}')
                plt.figure(1)
                plt.clf()
                plt.imshow(image)
                plt.title(f'Resized image {img} ')
                plt.pause(0.001)

    print(f'{i} images have been resized to size: {new_size}, with Image extension {out_format}')
