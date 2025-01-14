from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import pgettext_lazy

def list(
    request,
    filterset_class,
    model_list,
    fields_table,
    boolean_fields,
    url_variable,
    url_create_variable,
    title,
    template,
    file_fields,
):
    filterset = filterset_class(
        request.GET,
        queryset=model_list.objects.all().order_by("-id"),
    )
    filterset_form = filterset.form
    qs = filterset.qs
    paginator = Paginator(qs, 10)
    page_number = request.GET.get("page", 1)
    qs = paginator.get_page(page_number)
    ctx = {
        "filterset_form": filterset_form,
        "qs": qs,
        "fields_table": fields_table,
        "boolean_fields": boolean_fields,
        "title": title,
        "url_variable": url_variable,
        "url_create_variable": url_create_variable,
        "file_fields": file_fields,
    }
    return render(request, template, context=ctx)

def create_or_update(
    request,
    model,
    url_variable_create,
    url_variable_update,
    form_class,
    url_redirect_success,
    template,
    title,
    cancel_url,
    delete_url,
    model_name=None,
    pk=None,
    can_submit=True,
    can_delete=False
):
    instance = None
    url_variable = url_variable_create
    message = pgettext_lazy("Create or update view message", "Creation Success")
    if pk:
        instance = get_object_or_404(model, pk=pk)
        url_variable = url_variable_update
        message = pgettext_lazy("Create or update view message", "Update Success")
    form = form_class(request.POST or None,request.FILES or None, instance=instance, request=request)
    if form.is_valid():
        try:
            instance = form.save()
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(url_redirect_success)
        except Exception as e:
            messages.error(request, e.message)
    ctx = {
        "url_variable": url_variable,
        "form": form,
        "pk": pk,
        "title": title,
        "cancel_url": cancel_url,
        "delete_url": delete_url,
        "model_name": model_name,
        "can_submit": can_submit,
    }
    return render(request, template, context=ctx)

@login_required
def delete(
    request,
    pk,
    model,
    url_redirect_success,
    url_redirect_error,
    check_owner_field=None,
):
    instance = get_object_or_404(model, pk=pk)

    # Verificar si el usuario es el dueño (opcional)
    if check_owner_field:
        owner = getattr(instance, check_owner_field, None)
        if owner != request.user:
            messages.error(
                request,
                pgettext_lazy(
                    "Delete view message",
                    "You do not have permission to delete this object."
                ),
            )
            return redirect(url_redirect_error, pk=pk)

    try:
        instance.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            pgettext_lazy("Delete view message", "Deletion Success"),
        )
        return redirect(url_redirect_success)
    except Exception as e:
        messages.error(request, str(e))
        return redirect(url_redirect_error, pk=pk)
