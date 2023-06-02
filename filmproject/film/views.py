from django.shortcuts import render,redirect
from film.models import FilmModel, ActorModel,CommentModel,LikeModel,Category
# def isprime(n):
#     for i in range(2,n//2):
#         if n%i==0:
#             return False
#     return True


def index(request):
    films = FilmModel.objects.order_by("-name")
    categories = Category.objects.all()
    
    
    context = {
        "films" : films,
        "categories" : categories
        # "isprime": isprime(28)    
    }
    return render(request,'index.html', context)

def categoryfilms(request,id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    context = {
        "category" : category,
        "categories" : categories

    }
    return render (request,'categoryfilms.html',context)
#---------------------------------------------------------------

def detail(request,id):
    categories = Category.objects.all()
    film = FilmModel.objects.get(id=id)
    user_comments = CommentModel.objects.filter(
            user = request.user,
        ) if request.user.is_authenticated else None
    film_comments = CommentModel.objects.filter(
        film = film,
        parent = None
    )

    context = {
            "film" : film,
            "user_comments" : user_comments,
            "film_comments" : film_comments,
            "categories" : categories
        }

        
    if request.method == "POST":
        choice = request.POST.get("choice")
        if choice == "comment":
            comment = request.POST.get("comment")
            film_id = request.POST.get("film_id")

            film = FilmModel.objects.get(id=film_id)

            CommentModel.objects.create(
                user = request.user,
                film = film,
                comment = comment
            )
        elif choice =="like":
            film_id = request.POST.get("film_id")
            film = FilmModel.objects.get(id=film_id)
            
            if not LikeModel.objects.filter(user=request.user, film=film).exists():
                LikeModel.objects.create(
                    user = request.user,
                    film = film
                )
            else :
                like = LikeModel.objects.get(user=request.user, film=film)
                like.delete()
                
        elif choice == "reply":
            film_id = request.POST.get("film_id")
            film = FilmModel.objects.get(id=film_id)

            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id=comment_id)

            reply = request.POST.get("reply")
             
            CommentModel.objects.create(
                user = request.user,
                film = film,
                comment = reply,
                parent = comment
            )


        return redirect("detail",id=id)

    return render(request, 'detail.html', context)
#-----------------------------------------------------------
def actors(request,id):
    categories = Category.objects.all()
    actor = ActorModel.objects.get(id=id)
    user_comments = CommentModel.objects.filter(
        user = request.user,
    ) if request.user.is_authenticated else None
    actor_comments = CommentModel.objects.filter(
        actor = actor,
        parent = None
    )


    context = {
        "actor" : actor,
        "user_comments" : user_comments,
        "actor_comments" : actor_comments,
        "categories" : categories
    }

    if request.method == "POST":
        choice = request.POST.get("choice")
        if choice == "comment":
            comment = request.POST.get("comment")
            actor_id = request.POST.get("actor_id")

            actor = ActorModel.objects.get(id=actor_id)

            CommentModel.objects.create(
                user = request.user,
                actor = actor,
                comment = comment
            )
        elif choice =="like":
            actor_id = request.POST.get("actor_id")
            actor = ActorModel.objects.get(id=actor_id)

            if not LikeModel.objects.filter( user = request.user, actor = actor).exists():
                LikeModel.objects.create(
                    user = request.user,
                    actor = actor
                )
            else :
                like = LikeModel.objects.get(user=request.user, actor=actor)
                like.delete()

        elif choice == "reply":
            actor_id = request.POST.get("actor_id")
            actor = ActorModel.objects.get(id=actor_id)

            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id=comment_id)

            reply = request.POST.get("reply")
             
            CommentModel.objects.create(
                user = request.user,
                actor = actor,
                comment = reply,
                parent = comment
            )
        return redirect("actors",id=id)

    return render(request,'actors.html',context)
#------------------------------------------------------------------
def deleteComment(request,id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    return redirect("detail", id=comment.film.id)
#----------------------------------------------------------------
def deleteactorComment(request,id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    return redirect("actors", id=comment.actor.id)