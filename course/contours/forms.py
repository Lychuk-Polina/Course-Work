from django import forms
from contours.models import Img

class ImageForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ('image',)
