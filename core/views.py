from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import SignUpForm

from item.models import Category, Item
def index(request):
    items = Item.objects.filter(isSold=False)
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'items': items,
        'categories': categories,
    })

def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'auth/signup.html', {'form': form})