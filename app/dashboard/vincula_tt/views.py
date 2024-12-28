from django.contrib.auth.decorators import login_required
from django.utils.translation import pgettext_lazy

from core.views import list, create_or_update, delete
from apps.vincula_tt.models import *
from .filters import TrabajosTerminalesFilterSet
from .forms import TrabajosTerminalesForm

def list_tt(request):
    return list(
        request=request,
        filterset_class=TrabajosTerminalesFilterSet,
        model_list=TrabajosTerminales,
        fields_table={
            pgettext_lazy("Field table", "ID"): "pk",
            pgettext_lazy("Field table", "Title"): "titulo",
            pgettext_lazy("Field table", "TT Number"): "numero_tt",
            pgettext_lazy("Field table", "File"): "escrito.url",
        },
        boolean_fields=[],
        url_variable="tt-update",
        url_create_variable="tt-create",
        title=pgettext_lazy("List view title", "List of TT"),
        template="dashboard/vincula_tt/list.html",
        file_fields=["escrito.url"],
    )


def create_or_update_tt(request,pk=None):
    return create_or_update(
        request=request,
        model=TrabajosTerminales,
        url_variable_create="tt-create",
        url_redirect_success="tt-list",
        url_variable_update="tt-update",
        template="core/form.html",
        title=pgettext_lazy("Create or update view title", "TT"),
        pk=pk,
        cancel_url="tt-list",
        delete_url="",
        model_name=pgettext_lazy("Create or update view title", "TT"),
        form_class=TrabajosTerminalesForm,
        can_submit=not request.user.is_authenticated,
        )