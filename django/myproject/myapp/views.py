from django.shortcuts import render
# import your models (database api) to the views to pass to template
from .models import Feature

# Create your views here.


def index(request):
    # create a dictionary of key/values to send to html static page
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'Our service is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to Use'
    feature3.is_true = False
    feature3.details = 'Our service is very easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.is_true = True
    feature4.details = 'Our service is very affordable'

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {
        'features': features
        })

def counter(request):
    # to collect the words user is submitting in the form: get 'text' bc it's the same name attribute in the text area
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})