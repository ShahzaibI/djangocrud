from django.shortcuts import render, redirect
from vege.models import *
# Create your views here.


def create(request):
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipe/create/')
    query_set = Receipe.objects.all()
    
    if request.GET.get('search'):
        query_set = Receipe.objects.filter(receipe_name__icontains = request.GET.get('search'))
    context = {'receipes' : query_set}
    return render(request, 'create.html', context)

def delete(request, id):
    query_set = Receipe.objects.get(id = id)
    query_set.delete()
    return redirect('/receipe/create/')

def update(request, id):
    query_set = Receipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        query_set.receipe_name = receipe_name
        query_set.receipe_description = receipe_description
        if receipe_image:
            query_set.receipe_image = receipe_image
        query_set.save()
        return redirect('/receipe/create/')
    context = {'receipe' : query_set}
    return render(request, 'update.html', context)
