# from django.http import HttpResponse
# from django.contrib.auth import logout
from django.contrib.auth.views import login as django_login
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView

from .forms import SignupForm
# from .models import Profile


def login(request, template_name='registration/login.html'):
	if request.method == 'GET':
		response = django_login(request, template_name=template_name)
	elif request.method == 'POST':
		response = django_login(request, template_name=template_name)
		# 정상적으로 로그인이 됐을때
		if response.status_code == 302:
			# profile = Profile.objects.get(user=request.user)
			if not request.user.signup_approved:
				messages.error(request, "승인된 후 로그인이 가능합니다.")
				return HttpResponseRedirect("/accounts/logout")
	return response


def mypage(request):
	return render(request, 'accounts/mypage.html')


def signup(request):
	if request.method == 'POST':
		# form = UserCreationForm(request.POST)
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			User = get_user_model()
			user = User.objects.get(username=form.cleaned_data['username'])
			form.save_m2m()
			return redirect('accounts:login')
	else:
		# form = UserCreationForm()
		form = SignupForm()

	return render(request, 'accounts/signup.html', {'form': form})


class UserCreateView(CreateView):
	template_name = 'registration/register.html'
	form_class = SignupForm
	success_url = reverse_lazy('register_done')


def password_reset(request):
	form = PasswordChangeForm(request.user)
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			form.save()
			return redirect('accounts:logout')
	return render(request, 'accounts/password_reset.html', {'form': form})


def password_reset_admin(request):
	user = request.user
	if user.is_superuser:
		if request.method == 'POST':
			User = get_user_model()
			username = request.POST['username']
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				messages.error(request, "해당 아이디는 존재하지 않습니다.")
				return redirect('accounts:password_reset_admin')
			else:
				user.set_password('qwer1234')
				user.save()
		return render(request, 'accounts/admin_pw_reset.html')
	else:
		return redirect('notice:main')
