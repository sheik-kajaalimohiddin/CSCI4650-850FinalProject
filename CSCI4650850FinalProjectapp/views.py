from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

from CSCI4650850FinalProjectapp.forms import UploadImageForm
from CSCI4650850FinalProjectapp.models import ImagesUpload


# Create your views here.

def home(request):
    form = UploadImageForm()
    images = ImagesUpload.objects.all()
    return render(request,'CSCI4650850FinalProjectapp/index.html', {'form': form, 'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadImageForm()
    images = ImagesUpload.objects.all()
    return render(request, 'CSCI4650850FinalProjectapp/upload_image.html', {'form': form, 'images': images})

def delete_image(request, pk):
    image = ImagesUpload.objects.get(id=pk)
    if request.method=='POST':
        image.delete()
        return redirect('/upload/')
    context = {'item':image}
    return render(request, 'CSCI4650850FinalProjectapp/delete_image.html', context)


def search_image(request):
    return render(request,'CSCI4650850FinalProjectapp/searchImage.html')