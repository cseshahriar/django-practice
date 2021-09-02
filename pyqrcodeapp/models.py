from django.db import models

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Website(models.Model):
    name = models.CharField(max_length=100)
    qr_code =models.ImageField(upload_to='qe_code/', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        """ create qe_code """
        qrcode_img = qrcode.make(self.name) # name string is qrcode value
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False) # save false for infinit loop
        canvas.close()
        super().save(*args, **kwargs)

