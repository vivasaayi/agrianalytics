from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

from analytics.ml import ml
ml.load_models()

def handle_uploaded_file(f):
    file = f["file"]
    with open('media/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'analytics/index.html', {'form': form})

    return render(request, 'analytics/index.html', {})

def health(request):
    return HttpResponse("Hello, world!")



def predict_cifar(request):
    ml.predict_cifar()
    return HttpResponse("Hello, world. You're at the polls index.")