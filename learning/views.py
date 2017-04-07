from django.shortcuts import render, redirect, get_object_or_404
from .models import Learning, LearningComment
from .forms import LearningForm, LearningCommentForm
from Induk.decorators import is_article_active
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# def index(request):
#   return render(request, "learning/index.html")

@login_required
def learning_list(request):
    learning_list = Learning.objects.filter(show=True).order_by("-updated_at")
    paginator = Paginator(learning_list, 10)

    page = request.GET.get('page')

    try:
        learning_list = paginator.page(page)
    except PageNotAnInteger:
        learning_list = paginator.page(1)
    except EmptyPage:
        learning_list = paginator.page(paginator.num_pages)

    return render(request, "learning/learning_list.html", {
        "learning_list": learning_list,
    })


@login_required
@is_article_active
def learning_detail(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    return render(request, "learning/learning_detail.html", {
        "learning": learning,
        "comments": LearningComment.objects.filter(learning=learning),
        "comment_form": LearningCommentForm(),
    })


def learning_new(request):
    if request.method == "POST":
        form = LearningForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.show = True
            form.save()
            return redirect("learning:learning_detail", form.pk)
    else:
        form = LearningForm()
    return render(request, "learning/learning_form.html", {
        "form": form,
    })


@is_article_active
def learning_edit(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    if request.method == "POST":
        form = LearningForm(request.POST, instance=learning)
        if form.is_valid():
            form = form.save()
            return redirect("learning:learning_detail", learning.pk)
    else:
        form = LearningForm(instance=learning)
    return render(request, "learning/learning_form.html", {
        "form" : form,
    })


@is_article_active
def learning_del(request, pk):
    try:
        learning = Learning.objects.get(pk=pk)
    except Learning.DoesNotExist:
        return redirect('learning:learning_list')
    learning.show = False
    learning.save()

    return redirect('learning:learning_list')


@is_article_active
def learning_comment(request, pk):
    if request.method == 'POST':
        try:
            learning = Learning.objects.get(pk=pk)
        except Learning.DoesNotExist:
            return redirect('learning:learning_list')
        if not learning.show:
            return redirect('learning:learning_list')
        else:
            form = LearningCommentForm(request.POST)
            if form.is_valid():
                print('form valid')
                comment = form.save(commit=False)
                comment.author = request.user
                comment.learning = learning
                comment.save()
            return render(request, "learning/learning_comment_form.html", {
                "learning": learning,
                "comments": LearningComment.objects.filter(learning=learning),
                "comment_form": LearningCommentForm(),
            })
    return redirect('learning:learning_list')
