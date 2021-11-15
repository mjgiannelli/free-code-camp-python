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

def counter(request):
    # to collect the words user is submitting in the form: get 'text' bc it's the same name attribute in the text area
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})