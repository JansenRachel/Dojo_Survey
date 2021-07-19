from django.http import request
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')   

def process(request):
    if request.method == 'POST':
            context = {
            'name': request.POST['name'],
            'language':request.POST['Language'],
            'location':request.POST['Your Location'],
            'comment': request.POST['comment']
        }
    return render(request, 'result.html', context)
    return render(request, 'result.html')

# def result(request):
#     request.session['name'] = request.POST['name'],
#     request.session['language'] = request.POST['Language'],
#     request.session['location'] = request.POST['Your Location'],
#     request.session['comment'] =  request.POST['comment']




