from django.shortcuts import redirect, get_object_or_404, Http404
from django.contrib import messages
# from accounts.models import Profile
from report.models import Board, Report
from questions.models import Questions
from learning.models import Learning
from notice.models import Notice
# from django.contrib.auth import get_user_model


def is_signup_approved(view_func):
    def _decorator(request, *args, **kwargs):
        if not request.user.signup_approved:
            messages.error(request, "승인된 유저만 접근 가능합니다.")
            return redirect(request.META.get('HTTP_REFERER'))
        return view_func(request, *args, **kwargs)
    return _decorator


# def staff_required(view_func):
#     def _decorator(request, *args, **kwargs):
#         profile = Profile.objects.get(user=request.user)
#         if not profile.is_staff:
#             messages.error(request, "관리자만 접근 가능합니다.")
#             return redirect("notice:main")
#         return view_func(request, *args, **kwargs)
#     return _decorator


def is_company_active(view_func):
    def _decorator(request, *args, **kwargs):
        board = get_object_or_404(Board, company=kwargs['company'])
        if not board.active:
            messages.error(request, "비활성화된 회사입니다.")
            return redirect("report:report_index")
        return view_func(request, *args, **kwargs)
    return _decorator


def is_article_active(view_func):
    def _decorator(request, *args, **kwargs):
        url_name = request.resolver_match.url_name
        if 'pk' not in kwargs:
            pass
        else:
            if 'report' in url_name:
                post = get_object_or_404(Report, pk=kwargs['pk'])
            elif 'question' in url_name:
                post = get_object_or_404(Questions, pk=kwargs['pk'])
            elif 'learning' in url_name:
                post = get_object_or_404(Learning, pk=kwargs['pk'])
            elif 'notice' in url_name:
                post = get_object_or_404(Notice, pk=kwargs['pk'])
            if not post.show:
                raise Http404('삭제된 게시물입니다.')
        return view_func(request, *args, **kwargs)
    return _decorator


def is_user_belong_to(view_func):
    def _decorator(request, *args, **kwargs):
        company_list = [board.company for board in Board.objects.filter(active=True).filter(user_set=request.user).order_by('order')]
        if 'pk' in kwargs:
            report = Report.objects.get(pk=kwargs['pk'])
            if report.board.company not in company_list:
                raise Http404("허가되지 않은 접근입니다. 관리자로부터 소속허가를 승인받으십시오.")
        else:
            if 'company' not in kwargs:
                raise Http404('허가되지 않은 접근입니다.')
        return view_func(request, *args, **kwargs)
    return _decorator
