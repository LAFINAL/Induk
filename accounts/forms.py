from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from report.models import Board
# from .models import Profile


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "비밀번호가 일치하지 않습니다.",
    }
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )
    company = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=Board.objects.filter(active=True),
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "company")



class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='아이디',
        help_text='필수항목입니다. 30자 이내로 입력하세요. (알파벳, 숫자, @/./+/-/_만 가능)',
        max_length=30,
    )
    signup_approved = forms.BooleanField(
        label='회원가입 승인',
        help_text='사용자가 해당 사이트에 로그인이 가능한지를 나타냅니다.',
        required=False,
    )
    is_active = forms.BooleanField(
        label='활성 여부',
        help_text='사용자의 계정을 삭제하는 대신 이것을 선택 해제하세요.',
        required=False,
    )
    is_staff = forms.BooleanField(
        label='관리자 권한',
        help_text='관리자 화면(현재 페이지)에 들어올 수 있는 권한을 허가합니다.',
        required=False,
    )
    # 어차피 그룹은 안보이게 지정해 놨음
    groups = forms.ModelMultipleChoiceField(
        label=('권한 지정 (관리자 권한 지정시 필수)'),
        required=False,
        queryset=Group.objects.all(),
        help_text='모든 게시글 삭제/수정 권한을 허가합니다. 선택을 해제하려면 control키를 누르고 클릭하세요.',
    )
    company = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=Board.objects.filter(active=True),
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "signup_approved", "is_active", "is_staff", "date_joined", "last_login", "company"]


    class Media:
        js = (settings.STATIC_URL + 'js/userform.js',)
