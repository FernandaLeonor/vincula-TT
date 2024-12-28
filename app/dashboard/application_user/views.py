from django.utils.translation import pgettext_lazy
from core.views import list, create_or_update, delete
from apps.application_user.models import User
from .forms import UserForm

def CreateUser(request):
    return create_or_update(
        request=request,
        model=User,
        url_variable_create="user-create",
        url_redirect_success="tt-list",
        url_variable_update="",
        template="core/form.html",
        title=pgettext_lazy("Create or update view title", "user"),
        pk=None,
        cancel_url="tt-list",
        delete_url="",
        model_name=pgettext_lazy("Create or update view title", "user"),
        form_class=UserForm,
        )