from django.db import models
from .algo import Canny
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.
class Img(models.Model):
    image = models.ImageField(upload_to='images')
    filtered = models.ImageField(upload_to='images')

    def __str__(self):
        return f'Img {self.pk}'
 
    def save(self, *args, **kwargs):
        
        # open image
        pil_img = Image.open(self.image)

        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = Canny(cv_img)

        # convert back to pil image
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        #self.image.save(str(self.image), ContentFile(image_png), save=False)
        self.filtered.save("image.jpg", ContentFile(image_png), save=False)


        super().save(*args, **kwargs)

