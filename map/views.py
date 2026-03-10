from django.shortcuts import render
from django.http import JsonResponse
from movies.models import RegionalMovieStat
from accounts.models import REGION_CHOICES
from django.conf import settings

def index(request):
    template_data = {'title': 'Local Popularity Map'}
    return render(request, 'map/index.html', {'template_data': template_data})

def regional_stats(request):
    data = {}
    for region_key, region_label in REGION_CHOICES:
        stats = (
            RegionalMovieStat.objects
            .filter(region=region_key)
            .select_related('movie')
            .order_by('-purchase_count')
        )
        data[region_key] = {
            'label': region_label,
            'movies': [
                {
                    'name': s.movie.name,
                    'purchase_count': s.purchase_count,
                    'image_url': request.build_absolute_uri(s.movie.image.url) if s.movie.image else None,
                }
                for s in stats
            ]
        }
    return JsonResponse(data)