from django.shortcuts import render

# Create your views here.
def Portaf(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portaf.html", {'projects':projects})
