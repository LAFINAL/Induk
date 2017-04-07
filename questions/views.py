from django.shortcuts import render, redirect, get_object_or_404
from .models import Questions, QuestionsComment
from .forms import QuestionsForm, QuestionsCommentForm
from Induk.decorators import is_article_active
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# def index(request):
# 	return render(request, "notice/index.html")


@login_required
def questions_list(request):
    questions_list = Questions.objects.filter(show=True).order_by("-updated_at")
    paginator = Paginator(questions_list, 10)

    page = request.GET.get('page')

    try:
        questions_list = paginator.page(page)
    except PageNotAnInteger:
        questions_list = paginator.page(1)
    except EmptyPage:
        questions_list = paginator.page(paginator.num_pages)

    return render(request, "questions/questions_list.html", {
        "questions_list": questions_list,
    })


@login_required
@is_article_active
def questions_detail(request, pk):
    questions = get_object_or_404(Questions, pk=pk)
    return render(request, "questions/questions_detail.html", {
        "questions" : questions,
        "comments": QuestionsComment.objects.filter(questions=questions),
        "comment_form": QuestionsCommentForm(),
    })


def questions_new(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.show = True
            form.save()
            return redirect("questions:questions_detail", form.pk)
    else:
        form = QuestionsForm()
    return render(request, "questions/questions_form.html", {
        "form": form,
    })


@is_article_active
def questions_edit(request, pk):
    questions = get_object_or_404(Questions, pk=pk)
    if request.method == "POST":
        form = QuestionsForm(request.POST, instance=questions)
        if form.is_valid():
            form = form.save()
            return redirect("questions:questions_detail", questions.pk)
    else:
        form = QuestionsForm(instance=questions)
    return render(request, "questions/questions_form.html", {
        "form": form,
    })


@is_article_active
def questions_del(request, pk):
    try:
        questions = Questions.objects.get(pk=pk)
    except Questions.DoesNotExist:
        return redirect('questions:questions_list')
    questions.show = False
    questions.save()
    return redirect('questions:questions_list')


@is_article_active
def questions_comment(request, pk):
    if request.method == 'POST':
        try:
            questions = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            return redirect('questions:questions_list')
        if not questions.show:
            return redirect('questions:questions_list')
        else:
            form = QuestionsCommentForm(request.POST)
            if form.is_valid():
                print('form valid-questions')
                comment = form.save(commit=False)
                comment.author = request.user
                comment.questions = questions
                comment.save()
            return render(request, 'questions/questions_comment_form.html',{
                'questions': questions,
                'comments': QuestionsComment.objects.filter(questions=questions),
                'comment_form': QuestionsCommentForm(),
            })
    return redirect('questions:questions_detail')
