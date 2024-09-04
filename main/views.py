from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275866',
        'name': 'Alvin',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)