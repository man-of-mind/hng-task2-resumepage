from django.shortcuts import render

# Create your views here.

#class HomePage(models.CreateView):
#    pass

def HomePage(request):
    return render(request, 'resumeApp/index.html')