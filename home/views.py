from django.shortcuts import render
import random
def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    template_data['quote'] = get_quote()
    return render(request, 'home/index.html', {'template_data': template_data})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})
# Create your views here.

def get_quote():
    return random.choice(quote_list)

quote_list=[
    '''"I'll be back." - Terminator, The Terminator (1984)''',
    '''"I see dead people." - Cole Sear, The Sixth Sense (1999)''',
    '''"You're gonna need a bigger boat." - Chief Martin Brody, Jaws (1975)''',
    '''"May the Force be with you." - Han Solo, Star Wars: A New Hope (1977)''',
    '''"I'm the king of the world!" - Jack Dawson, Titanic (1997)''',
    '''"O Captain, my Captain." - John Keating, Dead Poets Society (1989)''',
    '''"I think this is the beginning of a beautiful friendship." - Rick Blaine, Casablanca (1942)''',
    '''"The first rule of Fight Club is you do not talk about Fight Club." - Tyler Durden, Fight Club (1999)''',
    '''"Why so serious?" - The Joker, The Dark Knight (2008)''',
    '''"What? Like it's hard?" - Elle Woods, Legally Blonde (2001)''' ,
    '''"You weren't supposed to see this one. Refresh again." - Xavier Evans, Georgia Tech Tragedy (2026)''',
    '''"As a child, I yearned for the mines." - Steve, A Minecraft Movie (2025)''',
    '''"Dishonor on your cow!" - Mushu, Mulan (1998)''',
    '''"Where! Is! My! Super! Suit!" - Frozone, The Incredibles (2004)''',
    '''"Bye Felicia." - Craig Jones, Friday (1995)''',
    '''"Say that again." - Reed Richards, Fantasic Four (2015)''',
    '''"To Infinity, and Beyond!" - Buzz Lightyear, Toy Story (2001)''',
    '''"Houston, we have a problem." - Jack Swigert, Apollo 13 (1995)''',
    '''"As if." - Cher Horowitz, Clueless (1995)''',
    '''"I'm going to make him an offer he can't refuse." - Don Vito Corleone, The Godfather (1972)''',
    '''"Say hello to my little friend!" - Tony Montana, Scarface (1983)''',
    '''"With great power, comes great responsibility" - Uncle Ben, Spider-Man (2002)'''

]
