from django.http import HttpResponseRedirect
from django.shortcuts import render
from . models import todo_item

def sss(request):
    q=todo_item.objects.all()
    return render(request,'my_app/detail.html',{'all_items':q})

def add_todo(request):
    if request.method=="POST":
        a=request.POST['concept']
        if a.strip()!='':
            n=todo_item(concept=a)
            n.save()
    return HttpResponseRedirect('/')

def delete_todo(request,todo_id):
    if request.method=="POST":
        delete_item=todo_item.objects.get(id=todo_id)
        delete_item.delete()
    return HttpResponseRedirect('/')
