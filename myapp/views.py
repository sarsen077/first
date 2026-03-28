from django.shortcuts import render,get_object_or_404
from .models import phones,noutbook

def homepage(request):
    telephones = phones.objects.all()
    context = {
        'telefonlar': telephones
    }
    return render(request,'home.html',context=context)

def noutbokpage(request):
    noutbooks = noutbook.objects.all()
    context = {
        'noutbooklar': noutbooks
    }
    return render(request,'noutbooks.html',context=context)

def detail(request,id):
    telefon = get_object_or_404(phones,id=id)
    context = {
        'telefon': telefon
    }
    return render(request,'detail.html',context=context)