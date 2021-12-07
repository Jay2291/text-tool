from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

    dtext = request.POST.get('text', 'Text not entered')
    remvpunc = request.POST.get('remvpunc', 'off')
    capsf = request.POST.get('capsf', 'off')
    nwlremv = request.POST.get('nwlremv', 'off')
    exspcrmv = request.POST.get('exspcrmv', 'off')
    analyzed = ""
    if capsf == "on":
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.upper()
        params = {"analyzedt": analyzed}
        dtext = analyzed

    if (remvpunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"analyzedt": analyzed}
        dtext = analyzed

    if nwlremv == "on":
        analyzed = ""
        for char in dtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"analyzedt": analyzed}
        dtext = analyzed

    if exspcrmv == "on":
        analyzed = ""
        res = " ".join(dtext.split())
        analyzed = str(res)
        params = {"analyzedt": analyzed}
        dtext = analyzed

    elif (remvpunc, capsf, nwlremv, exspcrmv == "off"):
        analyzed = dtext
        params = {"analyzedt": analyzed}

    return render(request, 'analyze.html', params)

def aboutus(request):
    return render(request, 'aboutus.html')
