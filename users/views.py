from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # request.POST = DATA/DICT BY THE USER , data from our form 
        if form.is_valid():
            form.save() # admin wala site ma save hunxa 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username} !')
            return redirect('web-home')
    else:
        form = UserRegisterForm() # empty post 

    return render(request, 'register.html', {'form':form})
