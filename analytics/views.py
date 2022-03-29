from django.shortcuts import render

# Create your views here.


from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import UploadFileForm

from analytics.ml import ml
ml.load_models()

def handle_uploaded_file(f):
    file = f["file"]
    file_name = 'media/' + file.name
    with open(file_name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return  file_name

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = handle_uploaded_file(request.FILES)
            return HttpResponseRedirect('/analytics/predict_mnist?name={}'.format(file_name))
    else:
        form = UploadFileForm()
    return render(request, 'analytics/index.html', {'form': form})

    return render(request, 'analytics/index.html', {})

def health(request):
    return HttpResponse("Hello, world!")



def predict_cifar(request):
    ml.predict_cifar()
    return HttpResponse("Hello, world. You're at the polls index.")

def predict_mnist(request):
    file_name = request.GET.get("name")
    result = ml.predcit_mnist(file_name)

    return JsonResponse(result, safe=False)