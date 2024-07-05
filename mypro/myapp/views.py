from django.shortcuts import render,HttpResponse
from .models import rec
# Create your views here.
def index(request):
    ob=rec.objects.all()
    d={'obj':ob}
    return render(request,'index.html',d)
def sec(request):
    if request.method == 'POST':
        n=request.POST['name']
        e=request.POST['email']
        m=request.POST['message']
        obj=rec()
        obj.name=n
        obj.email=e
        obj.message=m
        try:
            obj.save()
            return HttpResponse("success")
        except:
            return HttpResponse("Failed")