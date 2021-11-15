from django.shortcuts import render, redirect
# in order to save info to User model in database and use auth method
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# import your models (database api) to the views to pass to template
from .models import Feature

# Create your views here.


def index(request):
    # # create a dictionary of key/values to send to html static page
    # this is the way to do it without a db actually set up

    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'Our service is very quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.is_true = True
    # feature2.details = 'Our service is very reliable'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to Use'
    # feature3.is_true = False
    # feature3.details = 'Our service is very easy to use'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.is_true = True
    # feature4.details = 'Our service is very affordable'

    # features = [feature1, feature2, feature3, feature4]

    # return render(request, 'index.html', {
    #     'features': features
    #     })

    ### connect the database to the views to pass to the template ###
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def counter(request):
    # to collect the words user is submitting in the form: get 'text' bc it's the same name attribute in the text area
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # check if email already exists
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')
            else:
                # save all of this information into Users database
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        # if the passwords do not equal each other, send a message notifying user and redirect back to register
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')