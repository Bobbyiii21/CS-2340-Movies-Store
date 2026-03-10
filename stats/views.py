from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from movies.models import Movie, Review
from cart.models import Item, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count

def index(request):
    template_data = {}
    template_data['title'] = 'Stats'
    return render(request, 'stats/index.html', {'template_data': template_data})

def users(request):
    template_data = {'title' : 'Users'}
    template_data['users'] = []
    users = User.objects.annotate(commentCount=Count('review')).order_by("-commentCount")
    for u in users:
        orders = Order.objects.filter(user=u)
        moviePurchases = 0
        for order in orders:
            items = Item.objects.filter(order=order)
            for item in items:
                moviePurchases += item.quantity
        template_data['users'].append({'user': u, 'count': u.commentCount, 'movie_purchases': moviePurchases})
    return render(request,'stats/users.html',{'template_data': template_data})

def see_orders(request, id):
    user = User.objects.filter(id=id)
    print(user)
    template_data = {}
    template_data['user'] = user[0]
    template_data['title'] = 'Orders'
    template_data['orders'] = Order.objects.filter(user=user[0])
    return render(request, 'stats/see_orders.html', {'template_data': template_data})

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