from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from user.models import Users
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    # context = []

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        student_number = request.POST.get('student_number')
        phonenumber = request.POST.get('phonenumber')
        information = request.POST.get('information')
        img = request.POST.get('img')

        # if User.objects.filter(username=request.POST.get('username')):
        #     context['error'] = 'Email has tacked!!'
        #     return render(request, 'user/register.html', context=context)

        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        
        if user:
            user_profile = Users(
                user = user,
                student_number = student_number,
                fname = fname,
                lname = lname,
                phonenumber = phonenumber,
                email = email,
                information = information,
                profile_img_path = img
            )
            user_profile.save()
            return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')