from django.shortcuts import render

# Create your views here.
def forgotPass(request):
    return render(request, 'authen/forgotPass.html')

def otp(request):
    return render(request, 'authen/otp.html')

def resetPass(request):
    return render(request, 'authen/resetPass.html')

def signUp(request):
    return render(request, 'authen/signUp.html')

def signIn(request):
    return render(request, 'authen/signIn.html')