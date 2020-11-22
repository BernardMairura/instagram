from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required



# Create your views here.

# @login_required(login_url='/accounts/login/')
def index(request):
    posts=Image.objects.all()
    return render(request,'index.html',{"posts":posts})



# @login_required(login_url='/accounts/login')
def single_image(request, photo_id):
    image = Image.objects.get(id = photo_id)
    return render(request, 'single_image.html', {'image':image})



def profile_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, './profile.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, './image.html',{"message":message})



# @login_required(login_url='/accounts/login/')
def post(request): 
    current_user = request.user
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.image_owner = current_user
            photo.save()
            return redirect('index')
    else:
        form = ImageUpload()
    return render(request, 'post.html', {"form": form})