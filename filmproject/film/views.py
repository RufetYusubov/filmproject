from django.shortcuts import render,redirect
from film.models import FilmModel, ActorModel,CommentModel,LikeModel,Category, FavouriteFilms
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic import View
# def isprime(n):
#     for i in range(2,n//2):
#         if n%i==0:
#             return False
#     return True

class IndexView(View):
    def get(self,request,*args,**kwargs):
        films = FilmModel.objects.order_by("-id")
        categories = Category.objects.all()

    
        search = request.GET.get("search")
        if search:
            films = FilmModel.objects.filter(
                name__contains = search
            ).order_by("-id")

            
        context = {
        "films" : films,
        "categories" : categories
        # "isprime": isprime(28)    
    }
        return render(request,"home.html",context)
    
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            film_id = request.POST.get("film_id")
            film = FilmModel.objects.get(id=film_id)
            favouritefilm = FavouriteFilms.objects.create(
                    user = request.user,
                    film = film
                    
                )
        return redirect("home")
#-----------------------------------------------------
        
# def index(request):
#     films = FilmModel.objects.order_by("-id")
#     categories = Category.objects.all()

    
#     search = request.GET.get("search")
#     if search:
#         films = FilmModel.objects.filter(
#             name__contains = search
#         ).order_by("-id")


#     if request.user.is_authenticated:
#         if request.method == "POST":
#             film_id = request.POST.get("film_id")
#             film = FilmModel.objects.get(id=film_id)
#             favouritefilm = FavouriteFilms.objects.create(
#                 user = request.user,
#                 film = film
                
#             )
    
    
#     context = {
#         "films" : films,
#         "categories" : categories
#         # "isprime": isprime(28)    
#     }
#     return render(request,'index.html', context)
#-----------------------------------------------------------------
class Categoryfilms(View):
    def get(self,request,id,*args,**kwargs):
        category = Category.objects.get(id=id)
        categories = Category.objects.all()
        context = {
            "category" : category,
            "categories" : categories

        }
        return render (request,'categoryfilms.html',context)

# def categoryfilms(request,id):
#     category = Category.objects.get(id=id)
#     categories = Category.objects.all()
#     context = {
#         "category" : category,
#         "categories" : categories

#     }
#     return render (request,'categoryfilms.html',context)
#---------------------------------------------------------------
class DetailView(View):
    def get(self,request,id,*args,**kwargs):
        categories = Category.objects.all()
        film = FilmModel.objects.get(id=id)
        
        film_comments = CommentModel.objects.filter(
            film = film,
            parent = None
        )

        context = {
                "film" : film,
                "film_comments" : film_comments,
                "categories" : categories
            }
        if request.user.is_authenticated :
            user_comments = CommentModel.objects.filter(
                    user = request.user,
                )
            context["user_comments"] = user_comments
        return render(request, 'detail.html', context)
    
    def post(self,request,id,*args,**kwargs):
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




# def detail(request,id):
#     categories = Category.objects.all()
#     film = FilmModel.objects.get(id=id)
    
#     user_comments = CommentModel.objects.filter(
#             user = request.user,
#         ) if request.user.is_authenticated else None
#     film_comments = CommentModel.objects.filter(
#         film = film,
#         parent = None
#     )

#     context = {
#             "film" : film,
#             "user_comments" : user_comments,
#             "film_comments" : film_comments,
#             "categories" : categories
#         }
        
#     if request.method == "POST":
#         choice = request.POST.get("choice")
#         if choice == "comment":
#             comment = request.POST.get("comment")
#             film_id = request.POST.get("film_id")

#             film = FilmModel.objects.get(id=film_id)

#             CommentModel.objects.create(
#                 user = request.user,
#                 film = film,
#                 comment = comment
#             )
#         elif choice =="like":
#             film_id = request.POST.get("film_id")
#             film = FilmModel.objects.get(id=film_id)
            
#             if not LikeModel.objects.filter(user=request.user, film=film).exists():
#                 LikeModel.objects.create(
#                     user = request.user,
#                     film = film
#                 )
#             else :
#                 like = LikeModel.objects.get(user=request.user, film=film)
#                 like.delete()
                
#         elif choice == "reply":
#             film_id = request.POST.get("film_id")
#             film = FilmModel.objects.get(id=film_id)

#             comment_id = request.POST.get("comment_id")
#             comment = CommentModel.objects.get(id=comment_id)

#             reply = request.POST.get("reply")
             
#             CommentModel.objects.create(
#                 user = request.user,
#                 film = film,
#                 comment = reply,
#                 parent = comment
#             )


#         return redirect("detail",id=id)

#     return render(request, 'detail.html', context)
#-----------------------------------------------------------
class ActorView(View):
    def get(self,request,id,*args,**kwargs):
        categories = Category.objects.all()
        actor = ActorModel.objects.get(id=id)
        actor_comments = CommentModel.objects.filter(
            actor = actor,
            parent = None
        )


        context = {
            "actor" : actor,
            "actor_comments" : actor_comments,
            "categories" : categories
        }
        if request.user.is_authenticated :
            user_comments = CommentModel.objects.filter(
                    user = request.user,
                )
            context["user_comments"] = user_comments
        return render(request,'actors.html',context)
    
    def post(self,request,id,*args,**kwargs):
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


# def actors(request,id):
#     categories = Category.objects.all()
#     actor = ActorModel.objects.get(id=id)
#     user_comments = CommentModel.objects.filter(
#         user = request.user,
#     ) if request.user.is_authenticated else None
#     actor_comments = CommentModel.objects.filter(
#         actor = actor,
#         parent = None
#     )


#     context = {
#         "actor" : actor,
#         "user_comments" : user_comments,
#         "actor_comments" : actor_comments,
#         "categories" : categories
#     }

#     if request.method == "POST":
#         choice = request.POST.get("choice")
#         if choice == "comment":
#             comment = request.POST.get("comment")
#             actor_id = request.POST.get("actor_id")

#             actor = ActorModel.objects.get(id=actor_id)

#             CommentModel.objects.create(
#                 user = request.user,
#                 actor = actor,
#                 comment = comment
#             )
#         elif choice =="like":
#             actor_id = request.POST.get("actor_id")
#             actor = ActorModel.objects.get(id=actor_id)

#             if not LikeModel.objects.filter( user = request.user, actor = actor).exists():
#                 LikeModel.objects.create(
#                     user = request.user,
#                     actor = actor
#                 )
#             else :
#                 like = LikeModel.objects.get(user=request.user, actor=actor)
#                 like.delete()

#         elif choice == "reply":
#             actor_id = request.POST.get("actor_id")
#             actor = ActorModel.objects.get(id=actor_id)

#             comment_id = request.POST.get("comment_id")
#             comment = CommentModel.objects.get(id=comment_id)

#             reply = request.POST.get("reply")
             
#             CommentModel.objects.create(
#                 user = request.user,
#                 actor = actor,
#                 comment = reply,
#                 parent = comment
#             )
#         return redirect("actors",id=id)

#     return render(request,'actors.html',context)
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
#------------------------------------------------------------------------------
class FavouriteFilm(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            raise Http404
        categories = Category.objects.all()
        favouritefilms = FavouriteFilms.objects.filter(
            user = request.user
        )

        context = {
            "favouritefilms" : favouritefilms,
            "categories" : categories
        }
        user_comments = CommentModel.objects.filter(
            user = request.user
        )
        user_likes = LikeModel.objects.filter(
            user = request.user
        )
        context["user_comments"] = user_comments
        context["user_likes"] = user_likes


        return render (request, 'favouritefilms.html',context)

# def favouritefilms(request):
#     if not request.user.is_authenticated:
#         raise Http404
#     user_comments = CommentModel.objects.filter(
#         user = request.user
#     )
#     user_likes = LikeModel.objects.filter(
#         user = request.user
#     )
#     favouritefilms = FavouriteFilms.objects.filter(
#         user = request.user
#     )

#     context = {
#         "favouritefilms" : favouritefilms,
#         "user_comments" : user_comments,
#         "user_likes" : user_likes
#     }

#     return render (request, 'favouritefilms.html',context)
#---------------------------------------------------------------------------------
def DeleteFavouriteFilms(request,id):
    favouritefilm = FavouriteFilms.objects.get(id=id)
    favouritefilm.delete()
    return redirect("myfavouritefilms")
  