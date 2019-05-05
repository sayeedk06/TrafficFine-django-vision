from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from google.cloud import vision
import io
from .forms import FineForm
from .models import Fine
from django.contrib import messages

# fine function starts here
"""The following fine function at first recieves the images given by the user
and saves it to the media folder. Then using google-vision api detects the
text from the number plate and saves it to the num variable,assigned inside
the for loop and finally saves the amount,the text detected from the picture
and the current user. And then it removes image from the media folder
as there is no need for the image anymore.
"""
@login_required
def fine(request):
    if request.method == 'POST' and request.FILES['myfile']:
        form = FineForm(request.POST)

        # upload file to media folder starts here
        uploaded_file = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        #upload files to media folder ends here

        #google-vision api text detection starts here
        client = vision.ImageAnnotatorClient()
        path = "media/"+uploaded_file.name
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        # image_context = vision.types.ImageContext(language_hints=["bn"])
        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')
        num = 0
        for text in texts[:1]:
            # print('\n"{0}"'.format(text.description))
            num = text.description

        #google-vision text detection ends here
        #saving number from number plate and amount assigned to the database starts here
        # if 'amount' in request.POST and request.POST['amount']:
        #     form = Fine(amount=request.POST['amount'],numberPlate=num,policeUsername=request.user)
        #     form.save()
        if form.is_valid():
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            temp = form.save(commit=False)
            temp.numberPlate = num
            temp.policeUsername = request.user
            temp.save()


        else:
            os.remove(os.path.join(settings.MEDIA_ROOT,str(uploaded_file.name) ))
            messages.success(request,('Invalid Field....'))
            return redirect('assignFine')




        #saving number ends here

        # removes uploaded image from the media folder
        os.remove(os.path.join(settings.MEDIA_ROOT,str(uploaded_file.name) ))
        messages.success(request,('Fine assigned successffully....'))
        return redirect('profile')
            # 'uploaded_file_url': uploaded_file_url)
    else:
        form = FineForm()
        messages.success(request,('Upload valid image and assign fine....'))
        return render(request,'assignFine/assignFine.html',{'forms':form})

# fine function ends here
