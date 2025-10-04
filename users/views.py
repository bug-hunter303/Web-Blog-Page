from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
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

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, # uploaded files like images
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated Successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form , 
        'p_form': p_form,
    }
    return render(request, 'profile.html',context)


