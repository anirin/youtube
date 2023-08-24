from django.http.response import HttpResponseNotAllowed
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Video, Comment
from .forms import VideoForm, CommentForm
from django.views import View

class IndexView(View):
    # template_name = "youtube/index.html"

    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()
        context = {'videos' : videos}
        return render(request, "youtube/index.html", context)

class CreateView(View):

    def get(self, request, *args, **kwargs):
        form = VideoForm()
        context = {'form': form}
        return render(request, 'youtube/create.html', context)

    def post(self, request, *args, **kwargs):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("youtube:index")
        else:
            form = VideoForm()
            context = {'form': form}
        return render(request, 'youtube/create.html', context)

class DetailView(View):
    # template_name = "youtube/detail.html"

    def get(self, request, video_id, *args, **kwargs):
        video = Video.objects.get(id = video_id)
        comments = Comment.objects.filter(video = video_id)
        form = CommentForm()
        context = {
            'video': video,
            "comments" : comments,
            "form" : form
        }
        return render(request, 'youtube/detail.html', context)

    def post(self, request, video_id, *args, **kwargs):
        # フォームの保存
        json    = {"error" : True}
        form    = CommentForm(request.POST) 
        if not form.is_valid():
            print("Validation Error")
            return JsonResponse(json)
        #わからん
        comment = form.save(commit=False)  # フォームの保存を一時停止し、ビデオの関連を設定
        comment.video_id = video_id
        comment.save()

        json["error"] = False
        #viewの更新
        context = {}
        context["comments"] = Comment.objects.filter(video = video_id)
        json["content"] = render_to_string("youtube/content.html", context, request)
        return JsonResponse(json)
