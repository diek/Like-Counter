from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import PostUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = PostUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = PostUser
        fields = ("email",)
