from django.shortcuts import render

# Create your views here.

def boot_download(request):
    return render(request,'boot_download.html')