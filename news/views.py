from django.shortcuts import render

# Create your views here.
from django.contrib.auth import REDIRECT_FIELD_NAME, login, authenticate
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return REDIRECT_FIELD_NAME('home')  # Replace 'home' with your desired redirect URL
    else:
        form = RegisterForm()
    return render(request, 'social_books/register.html', {'form': form})