from django import forms


class RegisterForm(forms.Form):
    uname = forms.CharField(label='姓名')
    upwd = forms.CharField(label='密码', widget=forms.PasswordInput)
    uemail = forms.EmailField(label='邮箱')
    uage = forms.IntegerField(label='年龄')
