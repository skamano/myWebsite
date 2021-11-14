from django.shortcuts import render
from django.http import FileResponse, Http404
from pathlib import Path

from mysite.settings import BASE_DIR
# from django.http import HttpResponse
# from django.template import loader
# Create your views here.
def pdf_view(request, pdfFile):
    try:
        print(pdfFile)
        return FileResponse(open(pdfFile, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        # print('File not found')
        raise Http404("Resume could not be loaded from my server. I have been notified and I will look into it as soon as I can!")

def index(request):
    # template = loader.get_template('home/index.html')
    # return HttpResponse("Welcome to my homepage!")
    # return HttpResponse(template.render({}, request))
    context = {}
    # return render(request, 'home/external/index.html', context)
    return render(request, 'home/external/windows-95-ui-kit/index.html', context)

def projects(request):
    # return HttpResponse("This is my project page.")
    context = {}
    return render(request, 'home/projects.html', context)

def contact(request):
    # return HttpResponse("This is my contact info.")
    context = {}
    return render(request, 'home/contact.html', context)

def resume(request):
    # template = loader.get_template('home/resume.html')
    # return HttpResponse("This is my Resume")
    context = {}
    return pdf_view(request, BASE_DIR / 'home/templates/home/Sean_Kamano_Resume.pdf')
    # return render(request, 'home/resume.html', context)

def aboutMe(request):
    # return HttpResponse("Here is some info and background on me")
    context = {}
    return render(request, 'home/aboutMe.html', context)


