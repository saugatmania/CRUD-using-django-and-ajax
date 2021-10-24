from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import UserRegistration
from .models import User
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    form = UserRegistration()
    user = User.objects.all()
    return render(request, 'enroll/home.html', {'form': form, 'user': user})


# @csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            uid = request.POST.get('userid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            if(uid == ''):
                ur = User(name=name, email=email, password=password)
            else:
                ur = User(id=uid, name=name, email=email, password=password)
            ur.save()
            userdata = User.objects.values()
            user_data = list(userdata)
        return JsonResponse({'status': 'Save', 'user_data': user_data})
    else:
        return JsonResponse({'status': 0})


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        user = User.objects.get(pk=id)
        user_data = {'id': user.id, 'name': user.name,
                     'email': user.email, 'password': user.password}
        return JsonResponse(user_data)
