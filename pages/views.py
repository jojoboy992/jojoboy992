from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse
from .models import Student
from .forms import *
from myProject.urls import *
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy


def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "display.html", context)


def avatarView(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("succes")
    else:
        form = StudentForm()
    return render(request, "student_img.html", {"form": form})


def uploadok(request):
    return HttpResponse("succesful")


# Create your views here.


class homePageView(ListView):
    model = Post
    template_name = "index.html"


class secondHomePageView(ListView):
    model = Student
    template_name = "student.html"


def loginView(request):
    return render(request, "index2.html")


class BlogDetailView(DetailView):
    model = Post
    template_name = "content_prev.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    form_class = PostForm


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    form_class = PostEditForm


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
