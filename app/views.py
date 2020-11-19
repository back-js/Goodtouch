from django.shortcuts import render
from .forms import ImageForm
import base64
from io import BytesIO

import sys
sys.path.insert(0, 'C:/Users/s_ois/PycharmProjects/goodtouch/modules/PSGAN/')
from demo import main

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance

            image = main(img_obj.image1,img_obj.image2)
            output = BytesIO()
            image.save(output, format='JPEG')
            im_data = output.getvalue()
            data_url = 'data:image/jpg;base64,' + base64.b64encode(im_data).decode()

            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'image':data_url})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})