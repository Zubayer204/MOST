from django.shortcuts import render


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
