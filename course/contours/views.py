from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.http import HttpResponse
from .models import Img
from contours.forms import ImageForm
# Create your views here.

class AnswerView(DetailView):
    template_name = 'contours/result.html'
    model = Img

class SortView(CreateView):
    template_name = 'contours/home.html'
    model = Img
    form_class = ImageForm

    def get_success_url(self):
        my_object = Img.objects.latest('pk')
        
        my_object.save()
        return f"result/{my_object.pk}"