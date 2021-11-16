import os
import io
import base64
from PIL import Image 
# from gtts import gTTS 
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import render
from .forms import ImageForm
from .prediction import predictCaption

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.cleaned_data['image']
            path = default_storage.save('temp/sample.jpg', ContentFile(filename.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            caption = predictCaption(tmp_file)
            print(caption)
            words_list = caption.split(' ')
            words_list = words_list[1:len(words_list)-1]
            caption = ' '.join(words_list)
            img = Image.open(filename) 
            data = io.BytesIO()
            img.save(data, "JPEG")
            encoded_img = base64.b64encode(data.getvalue())
            decoded_img = encoded_img.decode('utf-8')
            img_data = f"data:image/jpeg;base64,{decoded_img}"
            # audio_obj = gTTS(text=caption, lang='en', slow=False)
            # audio_obj.save("caption.mp3")

            context = {
                'caption' : caption,
                "img_data": img_data,
            }
            return render(request, 'webInterface/result.html', context)
    else:
        form = ImageForm()
    
    return render(request, "webInterface/index.html", {'form': form})



