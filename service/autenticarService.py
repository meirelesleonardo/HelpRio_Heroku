from django.contrib.auth import authenticate, login

def altenticar(username,password,request):
    user = authenticate(username=username, password=password, request=request)
    if user is not None:
        login(request, user)
        return 1
    else:
        return 0