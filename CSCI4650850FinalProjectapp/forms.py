from django import forms
from .models import ImagesUpload


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = ImagesUpload
        fields = ('image_name','image','image_type',)