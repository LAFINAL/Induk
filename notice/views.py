from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from .models import Notice, NoticeComment
from .forms import NoticeForm, NoticeCommentForm
from Induk.decorators import is_article_active

# def index(request):
# 	return render(request, "notice/index.html")


def index(request):
    if request.user.is_authenticated():
        return redirect('notice:main')
    return render(request, "index.html")


def main(request):
    if not request.user.is_authenticated():
        return redirect('notice:index')
    return render(request, 'main.html')


@login_required
def notice_list(request):
    notice_list = Notice.objects.filter(show=True).order_by("-updated_at")
    paginator = Paginator(notice_list, 10)

    page = request.GET.get('page')

    try:
        notice_list = paginator.page(page)
    except PageNotAnInteger:
        notice_list = paginator.page(1)
    except EmptyPage:
        notice_list = paginator.page(paginator.num_pages)

    return render(request, "notice/index.html", {
        "notice_list": notice_list,
    })


@login_required
@is_article_active
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, "notice/notice_detail.html", {
        "notice": notice,
        "comments": NoticeComment.objects.filter(notice=notice),
        "comment_form": NoticeCommentForm(),
    })


def notice_new(request):
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.show = True
            form.save()
            return redirect("notice:notice_detail", form.pk)
    else:
        form = NoticeForm()
    return render(request, "notice/notice_form.html", {
        "form": form,
    })


@is_article_active
def notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form = form.save()
            return redirect("notice:notice_detail", notice.pk)
    else:
        form = NoticeForm(instance=notice)
    return render(request, "notice/notice_form.html", {
        "form": form,
    })


@is_article_active
def notice_del(request, pk):
    try:
        notice = Notice.objects.get(pk=pk)
    except Notice.DoesNotExist:
        return redirect('notice:notice_list')
    notice.show = False
    notice.save()

    return redirect('notice:notice_list')


@is_article_active
def notice_comment(request, pk):
    if request.method == 'POST':
        try:
            notice = Notice.objects.get(pk=pk)
        except Notice.DoesNotExist:
            return redirect('notice:notice_list')
        if not notice.show:
            return redirect('notice:notice_list')
        else:
            form = NoticeCommentForm(request.POST)
            if form.is_valid():
                print('form valid')
                comment = form.save(commit=False)
                comment.author = request.user
                comment.notice = notice
                comment.save()
            return render(request, "notice/notice_comment_form.html",{
                "notice": notice,
                "comments": NoticeComment.objects.filter(notice=notice),
                "comment_form": NoticeCommentForm(),
            })
    return redirect('notice:notice_list')
