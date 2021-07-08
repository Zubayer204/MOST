from django.http import JsonResponse
from django.utils import timezone
from .models import Newsletter, Visitor
from base.views import get_client_ip


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

def track_visitor(request):
    if request.method == 'POST':
        ip_addr = get_client_ip(request)
        user_agent = request.META['HTTP_USER_AGENT']
        referer = request.META['HTTP_REFERER']
        # will have to change in production
        if "127.0.0.1" or "pythonanywhere.com" in referer:
            referer = "/"
        track = Visitor.objects.filter(ip=ip_addr, user_agent=user_agent, referer=referer)
        # print(request.POST)
        if track:
            track = track.first()
            pages_visited = track.get_pages()
            pages_visited.append(request.POST.get('r_url'))
            track.latitude = request.POST.get('lat')
            track.longitude = request.POST.get('lon')
            track.last_visited = timezone.now()
            track.set_pages(pages_visited)
            track.save()
            return JsonResponse({'success': True, 'id': track.id})
        
        new_loc = Visitor.objects.create(
            ip=ip_addr,
            latitude=request.POST.get('lat'),
            longitude=request.POST.get('lon'),
            user_agent=user_agent,
            referer=referer,
            last_visited=timezone.now()
        )
        new_loc.set_pages([request.POST.get('r_url')])
        new_loc.save()
        return JsonResponse({'success': True, 'id': new_loc.id})
