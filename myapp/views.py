from django.shortcuts import render
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