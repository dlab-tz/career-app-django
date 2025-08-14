from django.shortcuts import render, redirect 
from .forms import UserProfileForm

# Create your views here.
def add_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect('add_user_profile')
        
    else:
        form = UserProfileForm()

    return render(request, 'users/form.html',{'form': form})