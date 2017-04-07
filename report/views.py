from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

from Induk.decorators import is_company_active, is_article_active, is_user_belong_to

from .forms import ReportForm, ReportCommentForm
from .models import Board, Report, ReportComment


def report_index(request):
	user = request.user
	company_list = Board.objects.filter(active=True).filter(user_set=user).order_by('order')
	return render(request, 'report/report_index.html', {
		'company_list': company_list,
	})


@is_company_active
@is_user_belong_to
def report_list(request, company):
	report_list = Report.objects.filter(board__company__exact=company).filter(show=True).order_by('-updated_at')
	title = Board.objects.get(company=company)
	paginator = Paginator(report_list, 10)
	page = request.GET.get('page')

	try:
		report_list = paginator.page(page)
	except PageNotAnInteger:
		report_list = paginator.page(1)
	except EmptyPage:
		report_list = paginator.page(paginator.num_pages)

	return render(request, "report/report_list.html", {
		"report_list": report_list,
		'company': company,
		'title': title,
	})


@is_company_active
@is_article_active
@is_user_belong_to
def report_detail(request, company, pk):
	report = get_object_or_404(Report, pk=pk)
	return render(request, "report/report_detail.html", {
		'company': company,
		"report": report,
		'comments': ReportComment.objects.filter(report=report),
	})


@is_company_active
@is_user_belong_to
def report_new(request, company):
	if request.method == "POST":
		form = ReportForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.board = get_object_or_404(Board, company=company)
			form.save()
			return redirect(reverse("report:report_list", args=(company,)))
	else:
		form = ReportForm()
	return render(request, "report/report_form.html", {
		"form": form,
	})


@is_company_active
@is_article_active
@is_user_belong_to
def report_edit(request, company, pk):
	report = get_object_or_404(Report, pk=pk)
	if request.method == "POST":
		form = ReportForm(request.POST, instance=report)
		if form.is_valid():
			form = form.save()
			return redirect(reverse("report:report_detail", args=(company, pk)))
	else:
		form = ReportForm(instance=report)
	return render(request, "report/report_form.html", {
		"form": form,
	})


@is_company_active
@is_article_active
@is_user_belong_to
def report_del(request, company, pk):
	try:
		report = Report.objects.get(pk=pk)
	except Report.DoesNotExist:
		return redirect(reverse("report:report_list", args=(company,)))
	report.show = False
	report.save()

	return redirect(reverse("report:report_list", args=(company,)))


@is_company_active
@is_article_active
@is_user_belong_to
def report_comment(request, company, pk):
	if request.method == 'POST':
		try:
			report = Report.objects.get(pk=pk)
		except Report.DoesNotExist:
			return redirect('report:report_list')
		if not report.show:
			return redirect('report:report_list')
		else:
			form = ReportCommentForm(request.POST)
			if form.is_valid():
				print('form valid')
				comment = form.save(commit=False)
				comment.author = request.user
				comment.report = report
				comment.save()
			# return redirect(reverse("report:report_detail", args=(company, pk)))
			return render(request, "report/report_comment_form.html", {
				"report": report,
				"company": company,
				"comments": ReportComment.objects.filter(report=report),
				"comment_form": ReportCommentForm(),
			})
	return redirect(reverse("report:report_list", args=(company,)))
