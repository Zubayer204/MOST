from django.shortcuts import render
from django.http import JsonResponse
from .models import Newsletter


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    print(get_client_ip(request))
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def subscribe(request):
    if request.method == 'POST':
        if not request.POST.get('email'):
            return JsonResponse({
                'success': False,
                'msg': "Email field cannot be empty",
                'style': 'alert alert-danger alert-dismissible fade show'
            })
        new_subscriber = Newsletter.objects.create(
            ip=get_client_ip(request),
            email=request.POST.get('email')
        )
        new_subscriber.save()
        return JsonResponse({
            'success': True,
            'msg': "Congrats! You've successfully subscribed to our News Letter",
            'style': 'alert alert-success alert-dismissible fade show'
        })
