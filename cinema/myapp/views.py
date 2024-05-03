from django.shortcuts import render,redirect
from myapp.models import Movie
from django.views.generic import View
from myapp.forms import MovieForm
# create a new movie 

# view for listing all movies
# url:localhost:8000/movies/all
# method:get
# standards:camelCase 2nd word is uppercase,snake_case include _(function,variables),PascalCase(class Name),kabab-case

# def movie_list_view(request,*args,**kwargs):
#     # fetch all movies from Movie mode
#     # and return an html template
#     qs=Movie.objects.all()
#     # context dictionary("key":value)
#     return render(request,"movie_list.html",{"data":qs})

# fetch a specific movie
#localhost:8000/movies/{id}/
class MovieListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        return render(request,'movie_list.html',{'data':qs})

# Create movie
# url:localhost:8000/myapp/movies/add/
# method:get,post

class MovieCreateView(View):
    def get(self,request,*args,**kwargs): 
        form=MovieForm()
        return render(request,'movie_add.html',{"form":form})

    def post(self,request,*args,**kwargs):
        form=MovieForm(request.POST,files=request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            Movie.objects.create(**data)
            # form.save()
            return redirect('movie-list')
        return render(request,'movie_add.html',{"form":form})

# movie detail view
# url:localhost:8000/myapp/movies/{id}/
# method:get

class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs) #kwargs={"pk":6}
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,'movie_detail.html',{'data':qs})

# remove/delete specific movie
# url:localhost:8000/myapp/movies/{id}/remove/
# method:get

class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect('movie-list')

# updating a movie
# url:localhost:8000/myapp/movies/{id}/change/
# method:get,post

class MovieUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Movie.objects.get(id=id)
        form=MovieForm(instance=movie_object)
        return render(request,'movie_edit.html',{'form':form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Movie.objects.get(id=id)
        form=MovieForm(request.POST,instance=movie_object,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        else:
            return render(request,'movie_edit.html',{'form':form})
