from django.shortcuts import render

# Create your views here.


def index(request):
    # create a dictionary of key/values to send to html static page
    context = {
        'name': 'Mark',
        'age': 33,
        'nationality': 'American'
    }
    return render(request, 'index.html', context)
