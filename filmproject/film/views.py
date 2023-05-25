from django.shortcuts import render
from film.models import FilmModel, ActorModel,CommentModel
def isprime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True


def index(request):
    films = FilmModel.objects.order_by("-name")
    
    context = {
        "films" : films,
        "isprime": isprime(28)
    }
    return render(request,'index.html', context)

def detail(request,id):
    film = FilmModel.objects.get(id=id)

    context = {
        "film" : film,
    }
    if request.method == "POST":
        comment = request.POST.get("comment")
        film_id = request.POST.get("film_id")

        film = FilmModel.objects.get(id=film_id)

        CommentModel.objects.create(
            user = request.user,
            film = film,
            comment = comment
        )
    return render(request, 'detail.html', context)

