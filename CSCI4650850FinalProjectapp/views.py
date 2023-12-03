from profile import Profile

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from CSCI4650850FinalProjectapp.forms import UploadImageForm
from CSCI4650850FinalProjectapp.models import ImagesUpload


# Create your views here.

def home(request):
    form = UploadImageForm()
    images = ImagesUpload.objects.all()
    return render(request, 'CSCI4650850FinalProjectapp/index.html', {'form': form, 'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/upload/')
    else:
        form = UploadImageForm()
    images = ImagesUpload.objects.all()
    return render(request, 'CSCI4650850FinalProjectapp/upload_image.html', {'form': form, 'images': images})


def delete_image(request, pk):
    image = ImagesUpload.objects.get(id=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('/')
    context = {'item': image}
    return render(request, 'CSCI4650850FinalProjectapp/delete_image.html', context)


def search_image(request):
    return render(request, 'CSCI4650850FinalProjectapp/searchImage.html')


def about(request):
    return render(request, 'CSCI4650850FinalProjectapp/about.html')


def local_search(request):
    return render(request, 'CSCI4650850FinalProjectapp/local_search.html', {'title': 'local_search'})


class ImageTypeSearchView(ListView):
    model = ImagesUpload
    template_name='CSCI4650850FinalProjectapp/local_search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('image-type')
        return ImagesUpload.objects.filter(image_type=query)


def detailedView(request, pk):
    items = ImagesUpload.objects.get(id=pk)
    context = {'item': items, }
    return render(request, 'CSCI4650850FinalProjectapp/image_detail_view.html', context)