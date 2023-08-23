from django.http.response import HttpResponseNotAllowed
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

def index(request):
	videos = Video.objects.all()
	context = {'videos' : videos}
	return render(request, "youtube/index.html", context)

def create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("youtube:index")  # ビデオのリストへリダイレクト
    else:
        form = VideoForm()
    return render(request, 'youtube/create.html', {'form': form})

def detail(request, video_id):
    video = Video.objects.get(id = video_id)
    return render(request, 'youtube/detail.html', {'video': video})
