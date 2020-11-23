from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile,Comment,User
from django.contrib.auth.decorators import login_required



# Create your views here.

# @login_required(login_url='/accounts/login/')
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.order_by('-date_created')
    profiles = Profile.objects.order_by('-last_update')
    comment = Comment.objects.order_by('-date_commented')
    return render(request, 'index.html', {'images':images, 'profiles':profiles,  'comment':comment})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.id)
    images = Image.objects.all().filter(profile_id=current_user.id)
    return render(request, 'profile.html', {'images':images, 'profile':profile})



@login_required(login_url='/accounts/login')
def single_image(request, photo_id):
    image = Image.objects.get(id = photo_id)
    return render(request, 'single_image.html', {'image':image})


# def news_today(request):
#     date = dt.date.today()
#     news = Article.todays_news()
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():

#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']
#             recipient = NewsLetterRececiepients(name = name,email =email)
#             recipient.save()
#             send_welcome_email(name,email)

#             HttpResponseRedirect('news_today')

#     else:
#         form = NewsLetterForm()
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})
def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            new_user = User.objects.create_user(username=username, password=password)
            return redirect('play')
    else:
        form = UserCreationForm()

    return render(request, 'antonymapp/create_user.html', {'form': form})



def profile_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_user(search_term)
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


# @login_required(login_url='/accounts/login/')
def new_comment(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.save()
        return redirect('allTimelines')
    else:
        form = NewCommentForm()
    return render(request, 'new_comment.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_status(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = NewStatusForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
        return redirect('allTimelines')
    else:
        form = NewStatusForm()
    return render(request, 'new_status.html', {"form": form})