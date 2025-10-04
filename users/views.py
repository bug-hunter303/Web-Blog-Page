from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # request.POST = DATA/DICT BY THE USER , data from our form 
        if form.is_valid():
            form.save() # admin wala site ma save hunxa 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username} , You can LogIn now!')
            return redirect('login')
    else:
        form = UserRegisterForm() # empty post 

    return render(request, 'register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')
