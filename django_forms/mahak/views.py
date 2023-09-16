from django.shortcuts import render,redirect
from . forms import studentform
from django.http import HttpResponse
from . models import vivan

# Create your views here.
def student(request):
    if request.method=='POST':
        form = studentform(request.POST)
        if (form.is_valid):
            form.save()
        return redirect('read')
    else:
        form=studentform()
        return render(request,'mahak.html',{'form':form})
    
def read(request):
    obj=vivan.objects.all()
    return render(request,'read.html',{'data':obj})


def edit(request,id):
    ext=vivan.objects.get(id=id)
    if request.method=='POST':
        fm=studentform(request.POST,instance=ext)
        if fm.is_valid:
            fm.save()
            return redirect('read')
    else:
        fm=studentform(instance=ext)
        return render(request,'edit.html',{'fm':fm})


def delete(request,id):
    obj=vivan.objects.get(id=id)
    obj.delete()
    return redirect('read')
    

