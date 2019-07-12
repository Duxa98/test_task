from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Create your views here.

from user_list.models import AppUser

def user_create():
    pass

def users_list(request):
    MAX_OBJECTS = 20
    users = AppUser.objects.all()[:MAX_OBJECTS]
    data = {
        'results': list(users.values())
    }
    return JsonResponse(data)


def user_info(request, login):
    user = get_object_or_404(AppUser, login=login)
    data = {
        'results': {
            'user_id': user.user_id,
            'weight': user.weight,
            'creation_time': user.creation_time
        }
    }
    return JsonResponse(data)

def user_modify():
    pass

def user_del():
    pass