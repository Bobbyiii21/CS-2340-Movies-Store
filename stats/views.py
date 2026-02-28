from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from movies.models import Movie, Review
from cart.models import Item
from django.contrib.auth.decorators import login_required

def index(request):
    template_data = {}
    template_data['title'] = 'Stats'
    return render(request, 'stats/index.html', {'template_data': template_data})

def users(request):
    template_data = {}
    template_data['title'] = 'Stats'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'stats/users.html', {'template_data': template_data})

def movies(request):
    template_data = {}
    template_data['title'] = 'Stats'
    movies = Movie.objects.all()
    template_data['movies'] = []
    for movie_to_get in movies:
        items = Item.objects.filter(movie=movie_to_get)
        reviews = Review.objects.filter(movie=movie_to_get)
        purchase_amount = 0
        revenue = 0
        review_amount = len(reviews)
        for item in items:
            purchase_amount += item.quantity
            revenue += purchase_amount * movie_to_get.price
        template_data['movies'].append({'movie': movie_to_get, 'purchases': purchase_amount, 'revenue': revenue, 'reviews': review_amount})
    return render(request, 'stats/movies.html', {'template_data': template_data})
# Create your views here.
