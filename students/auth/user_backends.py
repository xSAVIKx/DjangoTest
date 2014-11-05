from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

__author__ = 'Iurii Sergiichuk <i.sergiichuk@samsung.com>'


class EmailOrUsernameModelBackend(ModelBackend):
    def get_user(self, username):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=username)
        except user_model.DoesNotExist:
            return None

    def authenticate(self, username=None, password=None, **kwargs):
        user_model = get_user_model()
        if username is None:
            email = kwargs.get('email')
            if self._is_valid_email(email):
                kwargs = {'email': email}
            else:
                kwargs = {'username': kwargs.get('username')}
        else:
            if self._is_valid_email(username):
                kwargs = {'email': username}
            else:
                kwargs = {'username': username}
        try:
            user = user_model.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None

    @staticmethod
    def _is_valid_email(email):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError

        try:
            validate_email(email)
            return True
        except ValidationError:
            return False