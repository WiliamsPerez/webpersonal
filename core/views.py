from django.shortcuts import render, HttpResponse



# Create vistas
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")


def Contact(request):
   return render(request, "core/contact.html")